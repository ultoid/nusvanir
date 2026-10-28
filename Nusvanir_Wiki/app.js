/**
 * NUSVANIR DUNGEON COMPENDIUM - ENGINE & SCRIPT
 * D&D Dungeon Master's Guide Edition with Live Editing, Theme Switcher, and Photo Inserter.
 */

class NusvanirWiki {
  constructor() {
    this.dbName = 'NusvanirWikiDB';
    this.dbVersion = 1;
    this.storeName = 'articles';
    this.db = null;
    this.articles = [];
    this.currentArticleId = null;
    this.isEditing = false;
    this.currentTheme = localStorage.getItem('nusvanir_theme') || 'parchment';
    
    // UI elements
    this.sidebarNav = document.getElementById('sidebarNav');
    this.contentArea = document.getElementById('contentArea');
    this.viewContainer = document.getElementById('viewContainer');
    this.editorContainer = document.getElementById('editorContainer');
    this.homeContainer = document.getElementById('homeContainer');
    this.searchInput = document.getElementById('searchInput');
    this.searchDropdown = document.getElementById('searchDropdown');
    this.breadcrumbs = document.getElementById('breadcrumbs');
    this.newArticleModal = document.getElementById('newArticleModal');
    this.backupModal = document.getElementById('backupModal');
    this.photoModal = document.getElementById('photoModal');
    this.toast = document.getElementById('toast');
    
    // Editor fields
    this.editTitle = document.getElementById('editTitle');
    this.editCategory = document.getElementById('editCategory');
    this.editSubcategory = document.getElementById('editSubcategory');
    this.editTextarea = document.getElementById('editTextarea');
    this.editPreview = document.getElementById('editPreview');

    // Photo Modal state
    this.selectedPhotoSource = null;
    this.selectedPhotoTargetInput = 'editTextarea'; // or 'newArtContent'
  }

  async init() {
    this.applyTheme(this.currentTheme);
    this.initMarkdown();
    await this.initDatabase();
    await this.loadArticles();
    this.bindEvents();
    this.renderVaultGallery();
    
    // Check URL hash for article routing or show Home
    const hash = window.location.hash.slice(1);
    if (hash) {
      const decoded = decodeURIComponent(hash);
      const article = this.articles.find(a => a.id === decoded || a.title.toLowerCase() === decoded.toLowerCase());
      if (article) {
        this.openArticle(article.id);
      } else {
        this.openHome();
      }
    } else {
      this.openHome();
    }
  }

  // ==========================================
  // D&D THEME SWITCHER
  // ==========================================
  toggleTheme() {
    const nextTheme = (this.currentTheme === 'parchment') ? 'grimoire' : 'parchment';
    this.applyTheme(nextTheme);
  }

  applyTheme(theme) {
    this.currentTheme = theme;
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('nusvanir_theme', theme);

    const btn = document.getElementById('themeToggleBtn');
    if (btn) {
      if (theme === 'parchment') {
        btn.innerHTML = `📜 Mode Perkamen`;
        btn.title = 'Beralih ke Mode Grimoire Kuno (Gelap)';
      } else {
        btn.innerHTML = `🔮 Mode Grimoire`;
        btn.title = 'Beralih ke Mode Perkamen D&D (Terang)';
      }
    }
  }

  initMarkdown() {
    if (typeof marked !== 'undefined') {
      marked.setOptions({
        gfm: true,
        breaks: true,
        headerIds: true
      });
    }
  }

  // ==========================================
  // INDEXEDDB STORAGE SYSTEM
  // ==========================================
  initDatabase() {
    return new Promise((resolve) => {
      const request = indexedDB.open(this.dbName, this.dbVersion);

      request.onupgradeneeded = (e) => {
        const db = e.target.result;
        if (!db.objectStoreNames.contains(this.storeName)) {
          db.createObjectStore(this.storeName, { keyPath: 'id' });
        }
      };

      request.onsuccess = (e) => {
        this.db = e.target.result;
        resolve();
      };

      request.onerror = (e) => {
        console.error('IndexedDB error:', e);
        resolve();
      };
    });
  }

  async loadArticles() {
    return new Promise(async (resolve) => {
      if (!this.db) {
        this.articles = window.NUSVANIR_SEED_DATA || [];
        this.buildSidebarTree();
        return resolve();
      }

      const tx = this.db.transaction([this.storeName], 'readonly');
      const store = tx.objectStore(this.storeName);
      const req = store.getAll();

      req.onsuccess = async () => {
        let stored = req.result;
        if (!stored || stored.length === 0) {
          const initialData = window.NUSVANIR_SEED_DATA || [];
          await this.saveInitialData(initialData);
          this.articles = initialData;
        } else {
          this.articles = stored;
        }
        this.buildSidebarTree();
        this.updateCategoryDatalists();
        resolve();
      };

      req.onerror = () => {
        this.articles = window.NUSVANIR_SEED_DATA || [];
        this.buildSidebarTree();
        resolve();
      };
    });
  }

  async saveInitialData(data) {
    if (!this.db) return;
    return new Promise((resolve) => {
      const tx = this.db.transaction([this.storeName], 'readwrite');
      const store = tx.objectStore(this.storeName);
      data.forEach(item => store.put(item));
      tx.oncomplete = () => resolve();
      tx.onerror = () => resolve();
    });
  }

  async saveArticleToDB(article) {
    if (!this.db) {
      const idx = this.articles.findIndex(a => a.id === article.id);
      if (idx !== -1) this.articles[idx] = article;
      else this.articles.push(article);
      return;
    }

    return new Promise((resolve) => {
      const tx = this.db.transaction([this.storeName], 'readwrite');
      const store = tx.objectStore(this.storeName);
      store.put(article);
      tx.oncomplete = () => {
        const idx = this.articles.findIndex(a => a.id === article.id);
        if (idx !== -1) this.articles[idx] = article;
        else this.articles.push(article);
        resolve();
      };
    });
  }

  async deleteArticleFromDB(id) {
    if (!this.db) {
      this.articles = this.articles.filter(a => a.id !== id);
      return;
    }

    return new Promise((resolve) => {
      const tx = this.db.transaction([this.storeName], 'readwrite');
      const store = tx.objectStore(this.storeName);
      store.delete(id);
      tx.oncomplete = () => {
        this.articles = this.articles.filter(a => a.id !== id);
        resolve();
      };
    });
  }

  // ==========================================
  // SIDEBAR HIERARCHY TREE
  // ==========================================
  buildSidebarTree() {
    this.sidebarNav.innerHTML = '';

    // Fixed Top Links
    const homeItem = document.createElement('div');
    homeItem.className = 'sidebar-nav-item' + (!this.currentArticleId ? ' active' : '');
    homeItem.innerHTML = `<span>⚔️</span> <b>Beranda Kompendium</b>`;
    homeItem.onclick = () => this.openHome();
    this.sidebarNav.appendChild(homeItem);

    const kodexItem = this.articles.find(a => a.id.includes('Kitab_Nusvanir_Kodex_Semesta'));
    if (kodexItem) {
      const kodexNav = document.createElement('div');
      kodexNav.className = 'sidebar-nav-item' + (this.currentArticleId === kodexItem.id ? ' active' : '');
      kodexNav.innerHTML = `<span>📜</span> <b>Kitab Kodex Semesta</b>`;
      kodexNav.onclick = () => this.openArticle(kodexItem.id);
      this.sidebarNav.appendChild(kodexNav);
    }

    const divider = document.createElement('div');
    divider.className = 'sidebar-header';
    divider.innerHTML = `<span>Indeks Kampanye & Lore</span> <span>${this.articles.length} Bab</span>`;
    this.sidebarNav.appendChild(divider);

    // Group articles by Category -> Subcategory
    const hierarchy = {};
    this.articles.forEach(art => {
      let cat = art.category || 'Lainnya';
      let sub = art.subcategory || 'Umum';

      if (!hierarchy[cat]) hierarchy[cat] = {};
      if (!hierarchy[cat][sub]) hierarchy[cat][sub] = [];
      hierarchy[cat][sub].push(art);
    });

    const categoryIcons = {
      '00_Kosmologi & Sejarah': '🌌',
      '00_Pedoman & Kodex': '📜',
      '01_Hukum Sihir': '🔮',
      '02_World': '🗺️',
      '03_Region': '🏰',
      '04_Ras': '🧬',
      '05_Karakter & Tokoh Penting': '👥',
      '06_Sistem Game & Ekonomi': '⚖️',
      '07_Bestiary': '🐉',
      '08_Story': '📖',
      '09_Maps': '🧭'
    };

    // Render Sorted Categories
    Object.keys(hierarchy).sort().forEach(catName => {
      const subcats = hierarchy[catName];
      let totalCatArticles = 0;
      Object.values(subcats).forEach(list => totalCatArticles += list.length);

      const catEl = document.createElement('div');
      catEl.className = 'tree-category';
      catEl.dataset.cat = catName;

      const icon = categoryIcons[catName] || '📜';
      const cleanCatName = catName.replace(/^[0-9]+_/, '').replace(/_/g, ' ');

      catEl.innerHTML = `
        <div class="tree-header">
          <div class="tree-header-left">
            <span class="tree-arrow">▶</span>
            <span>${icon}</span>
            <span>${cleanCatName}</span>
          </div>
          <span class="tree-count">${totalCatArticles}</span>
        </div>
        <div class="tree-sub-list"></div>
      `;

      const subListContainer = catEl.querySelector('.tree-sub-list');
      const header = catEl.querySelector('.tree-header');
      header.onclick = () => {
        catEl.classList.toggle('expanded');
      };

      // Render Subcategories
      Object.keys(subcats).sort().forEach(subName => {
        const artList = subcats[subName];
        artList.sort((a, b) => a.title.localeCompare(b.title));

        const subEl = document.createElement('div');
        subEl.className = 'tree-sub-group';
        const cleanSubName = subName.replace(/^[0-9]+_/, '').replace(/_/g, ' ');

        subEl.innerHTML = `
          <div class="tree-sub-header">
            <div style="display:flex; align-items:center; gap:6px;">
              <span class="tree-arrow">▶</span>
              <span>${cleanSubName}</span>
            </div>
            <span class="tree-count" style="font-size:0.65rem;">${artList.length}</span>
          </div>
          <div class="tree-articles-list"></div>
        `;

        const articlesListContainer = subEl.querySelector('.tree-articles-list');
        subEl.querySelector('.tree-sub-header').onclick = (e) => {
          e.stopPropagation();
          subEl.classList.toggle('expanded');
        };

        // Render Article Links
        artList.forEach(art => {
          const itemEl = document.createElement('div');
          itemEl.className = 'tree-article-item' + (this.currentArticleId === art.id ? ' active' : '');
          itemEl.textContent = art.title;
          itemEl.title = art.title;
          itemEl.onclick = (e) => {
            e.stopPropagation();
            this.openArticle(art.id);
          };
          articlesListContainer.appendChild(itemEl);
        });

        subListContainer.appendChild(subEl);
      });

      this.sidebarNav.appendChild(catEl);
    });
  }

  // ==========================================
  // ARTICLE VIEWING & RENDERING
  // ==========================================
  openArticle(id) {
    const article = this.articles.find(a => a.id === id);
    if (!article) return;

    this.currentArticleId = article.id;
    this.isEditing = false;
    window.location.hash = encodeURIComponent(article.id);

    // Switch Views
    this.homeContainer.style.display = 'none';
    this.editorContainer.classList.remove('active');
    this.viewContainer.style.display = 'block';

    // Render Breadcrumbs
    this.renderBreadcrumbs(article);

    // Render Article Meta
    document.getElementById('viewCategoryBadge').textContent = article.category.replace(/^[0-9]+_/, '');
    document.getElementById('viewTitle').textContent = article.title;
    document.getElementById('viewSubMeta').innerHTML = `
      <span>🏰 <b>Kawasan:</b> ${article.subcategory}</span>
      <span>📜 <b>Revisi:</b> ${article.updatedAt || 'Kanonik'}</span>
      <span>🆔 <code>${article.id}</code></span>
    `;

    // Process & Render Markdown
    let rawContent = article.content || '';
    
    // Strip YAML frontmatter if present for cleaner reading
    if (rawContent.startsWith('---')) {
      const endFm = rawContent.indexOf('---', 3);
      if (endFm !== -1) {
        rawContent = rawContent.slice(endFm + 3).trim();
      }
    }

    // Convert Obsidian Wiki Links [[Target|Text]] or [[Target]]
    rawContent = rawContent.replace(/\[\[(.*?)(?:\|(.*?))?\]\]/g, (match, target, alias) => {
      const displayText = alias || target;
      return `<a href="javascript:void(0)" onclick="app.navigateToTitle('${target.replace(/'/g, "\\'")}')" class="wiki-internal-link">✦ ${displayText}</a>`;
    });

    // Fix relative image links so they resolve properly from Nusvanir_Wiki
    rawContent = rawContent.replace(/!\[(.*?)\]\((.*?)\)/g, (match, alt, src) => {
      let resolvedSrc = src;
      if (!src.startsWith('http') && !src.startsWith('data:') && !src.startsWith('/') && !src.startsWith('../')) {
        resolvedSrc = '../' + src;
      }
      return `![${alt}](${resolvedSrc})`;
    });

    const parsedHtml = (typeof marked !== 'undefined') ? marked.parse(rawContent) : `<pre>${rawContent}</pre>`;
    document.getElementById('viewBody').innerHTML = parsedHtml;

    // Scroll to top
    this.contentArea.scrollTop = 0;

    // Update active highlight in sidebar
    this.updateSidebarHighlight();
  }

  renderBreadcrumbs(article) {
    const cleanCat = article.category.replace(/^[0-9]+_/, '');
    this.breadcrumbs.innerHTML = `
      <span class="breadcrumb-link" onclick="app.openHome()">Kompendium</span>
      <span class="breadcrumb-sep">⚔️</span>
      <span class="breadcrumb-link" onclick="app.filterCategory('${article.category}')">${cleanCat}</span>
      <span class="breadcrumb-sep">/</span>
      <span class="breadcrumb-link">${article.subcategory}</span>
      <span class="breadcrumb-sep">/</span>
      <span style="font-weight:700;">${article.title}</span>
    `;
  }

  updateSidebarHighlight() {
    document.querySelectorAll('.sidebar-nav-item, .tree-article-item').forEach(el => el.classList.remove('active'));

    if (!this.currentArticleId) {
      const home = this.sidebarNav.querySelector('.sidebar-nav-item');
      if (home) home.classList.add('active');
      return;
    }

    const current = this.articles.find(a => a.id === this.currentArticleId);
    if (!current) return;

    document.querySelectorAll('.tree-category').forEach(catEl => {
      if (catEl.dataset.cat === current.category) {
        catEl.classList.add('expanded');
        catEl.querySelectorAll('.tree-sub-group').forEach(subEl => {
          if (subEl.textContent.includes(current.subcategory)) {
            subEl.classList.add('expanded');
          }
        });
      }
    });

    document.querySelectorAll('.tree-article-item').forEach(item => {
      if (item.textContent.trim() === current.title.trim()) {
        item.classList.add('active');
      }
    });
  }

  navigateToTitle(title) {
    const clean = title.trim().toLowerCase();
    const article = this.articles.find(a => {
      return a.title.toLowerCase() === clean || 
             a.id.toLowerCase().includes(clean) ||
             a.id.toLowerCase().endsWith('/' + clean + '.md');
    });

    if (article) {
      this.openArticle(article.id);
    } else {
      this.showToast(`Gulungan "<b>${title}</b>" belum ditemukan dalam arsip.`);
    }
  }

  // ==========================================
  // HOME DASHBOARD
  // ==========================================
  openHome() {
    this.currentArticleId = null;
    this.isEditing = false;
    window.location.hash = '';

    this.viewContainer.style.display = 'none';
    this.editorContainer.classList.remove('active');
    this.homeContainer.style.display = 'block';

    this.breadcrumbs.innerHTML = `
      <span class="breadcrumb-link" style="font-weight:700;">Beranda Panduan Penjelajah (Dungeon Guide)</span>
    `;

    // Stats
    const totalDocs = this.articles.length;
    const categoriesSet = new Set(this.articles.map(a => a.category));
    const regionsCount = this.articles.filter(a => a.category.includes('Region')).length;

    document.getElementById('statTotalDocs').textContent = totalDocs;
    document.getElementById('statCategories').textContent = categoriesSet.size;
    document.getElementById('statRegions').textContent = regionsCount;

    this.renderHomeFeatured();
    this.updateSidebarHighlight();
  }

  renderHomeFeatured() {
    const listContainer = document.getElementById('homeRecentList');
    if (!listContainer) return;

    listContainer.innerHTML = '';
    const featured = this.articles.slice(0, 8);
    featured.forEach(art => {
      const card = document.createElement('div');
      card.className = 'quick-card';
      card.onclick = () => this.openArticle(art.id);

      const snippet = art.content.slice(0, 115).replace(/#+\s+/g, '').replace(/---[\s\S]*?---/g, '').trim() + '...';

      card.innerHTML = `
        <div>
          <div class="quick-card-icon">📜</div>
          <div class="quick-card-title">${art.title}</div>
          <div class="quick-card-desc">${snippet}</div>
        </div>
        <div style="font-size:0.75rem; color:var(--dnd-gold); margin-top:12px; font-weight:700;">
          Bab: ${art.category.replace(/^[0-9]+_/, '')}
        </div>
      `;
      listContainer.appendChild(card);
    });
  }

  // ==========================================
  // EDITOR SYSTEM (INPUT & EDIT)
  // ==========================================
  startEdit(article = null) {
    const target = article || this.articles.find(a => a.id === this.currentArticleId);
    if (!target) return;

    this.isEditing = true;
    this.homeContainer.style.display = 'none';
    this.viewContainer.style.display = 'none';
    this.editorContainer.classList.add('active');

    this.editTitle.value = target.title;
    this.editCategory.value = target.category;
    this.editSubcategory.value = target.subcategory;
    this.editTextarea.value = target.content;

    this.updateLivePreview();
    this.updateCategoryDatalists();
    this.editTextarea.focus();
  }

  updateLivePreview() {
    const raw = this.editTextarea.value;
    if (typeof marked !== 'undefined') {
      this.editPreview.innerHTML = marked.parse(raw);
    } else {
      this.editPreview.innerHTML = `<pre>${raw}</pre>`;
    }
  }

  cancelEdit() {
    if (this.currentArticleId) {
      this.openArticle(this.currentArticleId);
    } else {
      this.openHome();
    }
  }

  async saveCurrentEdit() {
    const title = this.editTitle.value.trim();
    const category = this.editCategory.value.trim() || 'Lainnya';
    const subcategory = this.editSubcategory.value.trim() || 'Umum';
    const content = this.editTextarea.value;

    if (!title) {
      alert('Judul gulungan/artikel tidak boleh kosong!');
      this.editTitle.focus();
      return;
    }

    const today = new Date().toISOString().split('T')[0];
    let article = this.articles.find(a => a.id === this.currentArticleId);

    if (article) {
      article.title = title;
      article.category = category;
      article.subcategory = subcategory;
      article.content = content;
      article.updatedAt = today;
    } else {
      const newId = (category + '/' + subcategory + '/' + title.replace(/\s+/g, '_') + '.md').replace(/\/+/g, '/');
      article = {
        id: newId,
        title: title,
        category: category,
        subcategory: subcategory,
        content: content,
        path: newId,
        updatedAt: today
      };
      this.currentArticleId = newId;
    }

    await this.saveArticleToDB(article);
    this.buildSidebarTree();
    this.updateCategoryDatalists();
    this.openArticle(article.id);
    this.showToast('⚔️ Naskah berhasil disimpan ke arsip kompendium!');
  }

  async deleteCurrentArticle() {
    if (!this.currentArticleId) return;
    const article = this.articles.find(a => a.id === this.currentArticleId);
    if (!article) return;

    if (confirm(`Apakah Anda yakin ingin memusnahkan gulungan "${article.title}" dari arsip?`)) {
      await this.deleteArticleFromDB(article.id);
      this.buildSidebarTree();
      this.openHome();
      this.showToast(`🗑️ Gulungan "${article.title}" telah dimusnahkan.`);
    }
  }

  // Formatting Toolbar Helper
  insertFormat(prefix, suffix = '') {
    const ta = this.editTextarea;
    const start = ta.selectionStart;
    const end = ta.selectionEnd;
    const text = ta.value;
    const selected = text.substring(start, end) || 'Teks';

    const replacement = prefix + selected + suffix;
    ta.value = text.substring(0, start) + replacement + text.substring(end);
    ta.selectionStart = start + prefix.length;
    ta.selectionEnd = start + prefix.length + selected.length;
    ta.focus();
    this.updateLivePreview();
  }

  // ==========================================
  // PHOTO INSERTER MODAL (LOCAL UPLOAD & GALLERY)
  // ==========================================
  openPhotoModal(targetTextareaId = 'editTextarea') {
    this.selectedPhotoTargetInput = targetTextareaId;
    this.selectedPhotoSource = null;
    document.getElementById('photoCaption').value = '';
    document.getElementById('photoUrlInput').value = '';
    document.getElementById('selectedPhotoPreviewBox').classList.remove('active');
    
    // Switch to first tab
    this.switchPhotoTab('tabGallery');
    this.photoModal.classList.add('active');
  }

  closePhotoModal() {
    this.photoModal.classList.remove('active');
  }

  switchPhotoTab(tabId) {
    document.querySelectorAll('.photo-tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.photo-tab-pane').forEach(p => p.classList.remove('active'));

    const activeBtn = document.querySelector(`[data-tab="${tabId}"]`);
    if (activeBtn) activeBtn.classList.add('active');

    const pane = document.getElementById(tabId);
    if (pane) pane.classList.add('active');
  }

  renderVaultGallery() {
    const grid = document.getElementById('vaultGalleryGrid');
    if (!grid) return;

    const images = window.NUSVANIR_VAULT_IMAGES || [];
    grid.innerHTML = '';

    images.forEach(img => {
      const item = document.createElement('div');
      item.className = 'vault-gallery-item';
      item.title = `${img.title} (${img.category})`;

      item.innerHTML = `
        <img src="${img.path}" alt="${img.title}" loading="lazy" onerror="this.src='https://via.placeholder.com/150?text=Gambar'">
        <div class="vault-gallery-item-title">${img.title}</div>
      `;

      item.onclick = () => {
        document.querySelectorAll('.vault-gallery-item').forEach(el => el.classList.remove('selected'));
        item.classList.add('selected');
        this.selectPhoto(img.path, img.title);
      };

      grid.appendChild(item);
    });
  }

  selectPhoto(src, defaultCaption = '') {
    this.selectedPhotoSource = src;
    const previewBox = document.getElementById('selectedPhotoPreviewBox');
    const previewImg = document.getElementById('selectedPhotoThumb');
    const captionInput = document.getElementById('photoCaption');

    previewImg.src = src;
    previewBox.classList.add('active');
    if (!captionInput.value && defaultCaption) {
      captionInput.value = defaultCaption;
    }
  }

  handleFileUpload(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = (e) => {
      const base64Data = e.target.result;
      const fileName = file.name.rsplit ? file.name.rsplit('.', 1)[0] : file.name;
      this.selectPhoto(base64Data, fileName);
    };
    reader.readAsDataURL(file);
  }

  confirmInsertPhoto() {
    let src = this.selectedPhotoSource;
    const urlInput = document.getElementById('photoUrlInput').value.trim();
    if (!src && urlInput) {
      src = urlInput;
    }

    if (!src) {
      alert('Pilih gambar dari galeri, unggah file, atau masukkan URL terlebih dahulu!');
      return;
    }

    const caption = document.getElementById('photoCaption').value.trim() || 'Ilustrasi Nusvanir';
    const align = document.getElementById('photoAlign').value;

    let photoMarkdown = '';
    if (align === 'center') {
      photoMarkdown = `\n\n<figure align="center">\n  <img src="${src}" alt="${caption}" style="max-width:85%; border-radius:3px;">\n  <figcaption>${caption}</figcaption>\n</figure>\n\n`;
    } else if (align === 'left') {
      photoMarkdown = `\n\n<figure style="float:left; margin:0 24px 18px 0; max-width:40%;">\n  <img src="${src}" alt="${caption}" style="width:100%;">\n  <figcaption>${caption}</figcaption>\n</figure>\n\n`;
    } else if (align === 'right') {
      photoMarkdown = `\n\n<figure style="float:right; margin:0 0 18px 24px; max-width:40%;">\n  <img src="${src}" alt="${caption}" style="width:100%;">\n  <figcaption>${caption}</figcaption>\n</figure>\n\n`;
    } else {
      // Standard full width
      photoMarkdown = `\n\n![${caption}](${src})\n*${caption}*\n\n`;
    }

    // Insert into target textarea
    const targetTextarea = document.getElementById(this.selectedPhotoTargetInput) || this.editTextarea;
    const start = targetTextarea.selectionStart;
    const end = targetTextarea.selectionEnd;
    const text = targetTextarea.value;

    targetTextarea.value = text.substring(0, start) + photoMarkdown + text.substring(end);
    targetTextarea.selectionStart = start + photoMarkdown.length;
    targetTextarea.selectionEnd = start + photoMarkdown.length;
    targetTextarea.focus();

    if (this.selectedPhotoTargetInput === 'editTextarea') {
      this.updateLivePreview();
    }

    this.closePhotoModal();
    this.showToast('📷 Foto berhasil disisipkan ke naskah!');
  }

  // ==========================================
  // MODAL: BUAT ARTIKEL BARU
  // ==========================================
  openNewArticleModal() {
    document.getElementById('newArtTitle').value = '';
    document.getElementById('newArtCategory').value = '03_Region';
    document.getElementById('newArtSubcategory').value = 'Mandala Kingdom';
    document.getElementById('newArtContent').value = `# Judul Gulungan\n\n> *Kutipan pembuka kisah atau firman sakral mengenai entitas ini.*\n\n## Gambaran Umum\nTulis deskripsi dan rincian di sini.\n\n## Fakta & Aturan Pertempuran\n- Karakteristik utama\n- Kelemahan dan taktik penaklukan\n\n## Catatan Master Penjara\nRahasia tersembunyi yang hanya diketahui oleh penjelajah ulung.`;
    this.newArticleModal.classList.add('active');
    document.getElementById('newArtTitle').focus();
  }

  closeNewArticleModal() {
    this.newArticleModal.classList.remove('active');
  }

  async submitNewArticle() {
    const title = document.getElementById('newArtTitle').value.trim();
    const category = document.getElementById('newArtCategory').value.trim() || 'Lainnya';
    const subcategory = document.getElementById('newArtSubcategory').value.trim() || 'Umum';
    const content = document.getElementById('newArtContent').value;

    if (!title) {
      alert('Judul naskah tidak boleh kosong!');
      return;
    }

    const today = new Date().toISOString().split('T')[0];
    const newId = (category + '/' + subcategory + '/' + title.replace(/\s+/g, '_') + '.md').replace(/\/+/g, '/');

    const newArticle = {
      id: newId,
      title: title,
      category: category,
      subcategory: subcategory,
      content: content,
      path: newId,
      updatedAt: today
    };

    await this.saveArticleToDB(newArticle);
    this.closeNewArticleModal();
    this.buildSidebarTree();
    this.updateCategoryDatalists();
    this.openArticle(newArticle.id);
    this.showToast(`✨ Gulungan baru "<b>${title}</b>" berhasil dicatat ke kompendium!`);
  }

  updateCategoryDatalists() {
    const cats = Array.from(new Set(this.articles.map(a => a.category))).sort();
    const subcats = Array.from(new Set(this.articles.map(a => a.subcategory))).sort();

    const catDatalist = document.getElementById('categoryDatalist');
    if (catDatalist) {
      catDatalist.innerHTML = cats.map(c => `<option value="${c}"></option>`).join('');
    }

    const subDatalist = document.getElementById('subcategoryDatalist');
    if (subDatalist) {
      subDatalist.innerHTML = subcats.map(s => `<option value="${s}"></option>`).join('');
    }
  }

  // ==========================================
  // REALTIME SEARCH AUTOCOMPLETE
  // ==========================================
  handleSearch(query) {
    const q = query.trim().toLowerCase();
    if (!q) {
      this.searchDropdown.classList.remove('active');
      return;
    }

    const matches = this.articles.filter(a => {
      return a.title.toLowerCase().includes(q) ||
             a.category.toLowerCase().includes(q) ||
             a.subcategory.toLowerCase().includes(q) ||
             a.content.toLowerCase().includes(q);
    }).slice(0, 10);

    if (matches.length === 0) {
      this.searchDropdown.innerHTML = `<div style="padding:14px; text-align:center; color:var(--text-dim); font-style:italic;">Tidak ada gulungan tercatat untuk "${query}"</div>`;
      this.searchDropdown.classList.add('active');
      return;
    }

    this.searchDropdown.innerHTML = '';
    matches.forEach(m => {
      const item = document.createElement('div');
      item.className = 'search-item';
      item.innerHTML = `
        <span class="search-item-title">${m.title}</span>
        <span class="search-item-cat">${m.category.replace(/^[0-9]+_/, '')} / ${m.subcategory}</span>
      `;
      item.onclick = () => {
        this.openArticle(m.id);
        this.searchDropdown.classList.remove('active');
        this.searchInput.value = '';
      };
      this.searchDropdown.appendChild(item);
    });

    this.searchDropdown.classList.add('active');
  }

  // ==========================================
  // BACKUP & EXPORT/IMPORT MODAL
  // ==========================================
  openBackupModal() {
    this.backupModal.classList.add('active');
  }

  closeBackupModal() {
    this.backupModal.classList.remove('active');
  }

  exportData() {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(this.articles, null, 2));
    const downloadAnchor = document.createElement('a');
    downloadAnchor.setAttribute("href", dataStr);
    const date = new Date().toISOString().split('T')[0];
    downloadAnchor.setAttribute("download", `Nusvanir_Compendium_Backup_${date}.json`);
    document.body.appendChild(downloadAnchor);
    downloadAnchor.click();
    downloadAnchor.remove();
    this.showToast('📥 Gulungan cadangan kompendium berhasil diunduh!');
  }

  importData(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = async (e) => {
      try {
        const imported = JSON.parse(e.target.result);
        if (Array.isArray(imported)) {
          if (confirm(`Impor ${imported.length} gulungan dari file cadangan? Seluruh arsip saat ini akan diperbarui.`)) {
            await this.saveInitialData(imported);
            this.articles = imported;
            this.buildSidebarTree();
            this.closeBackupModal();
            this.openHome();
            this.showToast(`✅ Berhasil memulihkan ${imported.length} naskah!`);
          }
        } else {
          alert('Format naskah JSON tidak sah!');
        }
      } catch (err) {
        alert('Gagal membaca berkas: ' + err.message);
      }
    };
    reader.readAsText(file);
  }

  async resetData() {
    if (confirm('Kembalikan seluruh naskah kompendium ke kondisi awal Nusvanir Vault? Semua suntingan manual akan diselaraskan ulang.')) {
      const seed = window.NUSVANIR_SEED_DATA || [];
      await this.saveInitialData(seed);
      this.articles = seed;
      this.buildSidebarTree();
      this.closeBackupModal();
      this.openHome();
      this.showToast('🔄 Arsip kompendium dikembalikan ke data kanonik vault.');
    }
  }

  showToast(message) {
    this.toast.innerHTML = message;
    this.toast.classList.add('show');
    clearTimeout(this.toastTimer);
    this.toastTimer = setTimeout(() => {
      this.toast.classList.remove('show');
    }, 3500);
  }

  bindEvents() {
    // Search listener
    this.searchInput.addEventListener('input', (e) => this.handleSearch(e.target.value));
    
    // Close dropdown on outside click
    document.addEventListener('click', (e) => {
      if (!this.searchInput.contains(e.target) && !this.searchDropdown.contains(e.target)) {
        this.searchDropdown.classList.remove('active');
      }
    });

    // Keyboard shortcut Ctrl+K to search
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        this.searchInput.focus();
        this.searchInput.select();
      }
    });

    // Editor textarea live preview
    this.editTextarea.addEventListener('input', () => this.updateLivePreview());

    // Direct Clipboard Paste (Ctrl+V) Image Support inside Editor!
    this.editTextarea.addEventListener('paste', (e) => {
      const items = (e.clipboardData || e.originalEvent.clipboardData).items;
      for (let item of items) {
        if (item.kind === 'file' && item.type.startsWith('image/')) {
          e.preventDefault();
          const blob = item.getAsFile();
          const reader = new FileReader();
          reader.onload = (event) => {
            const base64 = event.target.result;
            const snippet = `\n\n![Tangkapan Gambar](${base64})\n*Tangkapan Gambar Dokumen*\n\n`;
            this.insertFormat(snippet);
            this.showToast('📷 Gambar dari clipboard berhasil ditempelkan!');
          };
          reader.readAsDataURL(blob);
          break;
        }
      }
    });

    // Direct Drag and Drop Image into textarea!
    this.editTextarea.addEventListener('dragover', (e) => e.preventDefault());
    this.editTextarea.addEventListener('drop', (e) => {
      e.preventDefault();
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {
        const file = e.dataTransfer.files[0];
        if (file.type.startsWith('image/')) {
          const reader = new FileReader();
          reader.onload = (event) => {
            const base64 = event.target.result;
            const snippet = `\n\n![${file.name}](${base64})\n*${file.name}*\n\n`;
            this.insertFormat(snippet);
            this.showToast(`📷 Berkas "${file.name}" berhasil ditarik dan disisipkan!`);
          };
          reader.readAsDataURL(file);
        }
      }
    });
  }
}

// Global App Instance
const app = new NusvanirWiki();
document.addEventListener('DOMContentLoaded', () => {
  app.init();
});
