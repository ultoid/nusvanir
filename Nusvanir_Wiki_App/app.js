document.addEventListener('DOMContentLoaded', () => {
    const categoryNav = document.getElementById('categoryNav');
    const contentArea = document.getElementById('contentArea');
    const pageTitle = document.getElementById('pageTitle');
    const searchInput = document.getElementById('searchInput');

    // Root node for tree
    const tree = {};
    
    if (typeof nusvanirDB !== 'undefined') {
        nusvanirDB.forEach(item => {
            const parts = item.folderPath.split('/');
            let current = tree;
            parts.forEach(part => {
                if (!current[part]) {
                    current[part] = { _files: [], _sub: {} };
                }
                current = current[part]._sub;
            });
            
            // Navigate to the folder to push the file
            let folder = tree;
            parts.forEach(part => {
                folder = folder[part];
                if(part !== parts[parts.length-1]) folder = folder._sub;
            });
            folder._files.push(item);
        });
    }

    // Render Home
    renderHome();

    // Add Home Button to Sidebar
    const homeBtn = document.createElement('div');
    homeBtn.className = 'nav-item active root-nav';
    homeBtn.innerHTML = `<span><i class="icon">🏠</i> Beranda</span>`;
    homeBtn.onclick = () => {
        setActiveNav(homeBtn);
        renderHome();
    };
    categoryNav.appendChild(homeBtn);

    // Build hierarchical sidebar
    // Sort top level folders by their name (this naturally sorts 00_, 01_, 02_, etc.)
    const rootFolders = Object.keys(tree).sort();
    
    rootFolders.forEach(folderName => {
        const folderNode = tree[folderName];
        buildNavNode(categoryNav, folderName, folderNode, 0);
    });

    function buildNavNode(parentEl, folderName, node, depth) {
        // Wrapper for the whole accordion item
        const wrapper = document.createElement('div');
        wrapper.className = 'nav-folder-wrapper';
        
        // The clickable header
        const header = document.createElement('div');
        header.className = 'nav-item';
        header.style.paddingLeft = `${0.8 + (depth * 1)}rem`;
        
        // Count total files in this node recursively
        const totalFiles = countFiles(node);
        
        header.innerHTML = `
            <span class="folder-title">
                <span class="chevron">▶</span> 
                ${folderName}
            </span> 
            <span class="count">${totalFiles}</span>
        `;
        
        // The container for children (hidden by default)
        const childrenContainer = document.createElement('div');
        childrenContainer.className = 'nav-children';
        childrenContainer.style.display = 'none';
        
        header.onclick = (e) => {
            e.stopPropagation();
            const isHidden = childrenContainer.style.display === 'none';
            childrenContainer.style.display = isHidden ? 'block' : 'none';
            header.querySelector('.chevron').textContent = isHidden ? '▼' : '▶';
            
            setActiveNav(header);
            // Render this folder's contents as a grid
            const allItems = getAllFiles(node);
            renderGrid(allItems, folderName);
        };
        
        wrapper.appendChild(header);
        
        // Sub folders
        const subFolders = Object.keys(node._sub).sort();
        subFolders.forEach(subName => {
            buildNavNode(childrenContainer, subName, node._sub[subName], depth + 1);
        });
        
        // Files in this folder
        if(node._files && node._files.length > 0) {
            // Sort files by name
            node._files.sort((a,b) => a.title.localeCompare(b.title)).forEach(file => {
                const fileEl = document.createElement('div');
                fileEl.className = 'nav-item file-item';
                fileEl.style.paddingLeft = `${1.5 + (depth * 1)}rem`;
                fileEl.innerHTML = `<span class="file-title">📄 ${file.title}</span>`;
                
                fileEl.onclick = (e) => {
                    e.stopPropagation();
                    setActiveNav(fileEl);
                    renderDetail(file);
                };
                
                childrenContainer.appendChild(fileEl);
            });
        }
        
        wrapper.appendChild(childrenContainer);
        parentEl.appendChild(wrapper);
    }
    
    function countFiles(node) {
        let count = node._files ? node._files.length : 0;
        Object.values(node._sub).forEach(subNode => {
            count += countFiles(subNode);
        });
        return count;
    }

    function getAllFiles(node) {
        let files = node._files ? [...node._files] : [];
        Object.values(node._sub).forEach(subNode => {
            files = files.concat(getAllFiles(subNode));
        });
        return files;
    }

    // Search functionality
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase();
        if (query.length < 2) {
            if (query.length === 0) renderHome();
            return;
        }

        const results = nusvanirDB.filter(item => 
            (item.title && item.title.toLowerCase().includes(query)) ||
            (item.content && item.content.toLowerCase().includes(query))
        );

        renderGrid(results, `Hasil Pencarian: "${query}"`);
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
    });

    function setActiveNav(element) {
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));
        if(element) element.classList.add('active');
    }

    function renderHome() {
        pageTitle.textContent = "Beranda";
        
        let html = `
            <div class="markdown-body" style="text-align: center; margin-bottom: 3rem;">
                <h1 style="border: none; margin-bottom: 0.5rem; font-size: 3.5rem;">Selamat Datang di Nusvanir</h1>
                <p style="color: var(--text-muted); font-size: 1.2rem; max-width: 800px; margin: 0 auto;">
                    Nusvanir adalah sebuah semesta fantasi gelap (Dark Fantasy) yang terinspirasi dari kekayaan mitologi, budaya, dan sejarah Nusantara. Di dunia ini, kekuatan elemen alam bertabrakan dengan sihir kuno, faksi-faksi saling memperebutkan pengaruh, dan monster-monster legenda berkeliaran di alam liar. Jelajahi pengetahuan terlarang, pahlawan epik, dan rahasia terdalam dari benua Nusvanir.
                </p>
            </div>
            <h2 style="margin-bottom: 1.5rem; color: var(--accent); border-bottom: 1px solid var(--border-glass); padding-bottom: 0.5rem;">Pilih Pintu Penjelajahan Anda:</h2>
            <div class="grid-container" id="worldChoices">
            </div>
        `;
        
        contentArea.innerHTML = html;
        
        const worldChoices = document.getElementById('worldChoices');
        
        // Define big buttons for the top level folders
        const rootFolders = Object.keys(tree).sort();
        rootFolders.forEach(folderName => {
            const card = document.createElement('div');
            card.className = 'card category-card';
            
            const count = countFiles(tree[folderName]);
            
            // Clean name for display (remove 00_)
            const cleanName = folderName.replace(/^[0-9]+_/, '').replace(/_/g, ' ');
            
            // Pick an icon based on name
            let icon = '📚';
            if(cleanName.includes('Sejarah')) icon = '⏳';
            else if(cleanName.includes('Sihir')) icon = '✨';
            else if(cleanName.includes('World')) icon = '🌍';
            else if(cleanName.includes('Region')) icon = '🗺️';
            else if(cleanName.includes('Ras')) icon = '👥';
            else if(cleanName.includes('Karakter')) icon = '👑';
            else if(cleanName.includes('Sistem')) icon = '⚖️';
            else if(cleanName.includes('Bestiary')) icon = '🐉';
            
            card.innerHTML = `
                <div style="font-size: 3rem; margin-bottom: 1rem; text-align: center;">${icon}</div>
                <h3 style="text-align: center;">${cleanName}</h3>
                <p style="text-align: center;">Total Entitas: ${count}</p>
            `;
            
            card.onclick = () => {
                const allItems = getAllFiles(tree[folderName]);
                renderGrid(allItems, folderName);
                
                // Try to expand the sidebar corresponding to this folder
                const sidebarItems = document.querySelectorAll('.nav-folder-wrapper > .nav-item');
                sidebarItems.forEach(el => {
                    if (el.textContent.includes(folderName)) {
                        const children = el.nextElementSibling;
                        if (children && children.style.display === 'none') {
                            el.click(); // simulate click to open
                        }
                    }
                });
            };
            
            worldChoices.appendChild(card);
        });
    }

    function renderGrid(items, title) {
        pageTitle.textContent = title.replace(/^[0-9]+_/, '').replace(/_/g, ' ');
        contentArea.innerHTML = '';
        const gridDiv = document.createElement('div');
        gridDiv.className = 'grid-container';
        contentArea.appendChild(gridDiv);
        
        if(items.length === 0) {
            gridDiv.innerHTML = `<p style="color: var(--text-muted); grid-column: 1/-1;">Tidak ada data ditemukan.</p>`;
            return;
        }
        
        items.forEach(item => {
            const card = document.createElement('div');
            card.className = 'card';
            
            let rawContent = item.content || "";
            if (rawContent.startsWith("---")) {
                const parts = rawContent.split("---");
                if (parts.length >= 3) {
                    rawContent = parts.slice(2).join("---").trim();
                }
            }
            
            // Remove markdown characters, newlines, and truncate
            let snippet = rawContent.replace(/[#*`_\[\]\n\r]/g, ' ').replace(/\s+/g, ' ').trim();
            if(snippet.length > 120) snippet = snippet.substring(0, 120) + "...";
            
            card.innerHTML = `
                ${item.element ? `<div class="badge">${item.element}</div>` : ''}
                <h3>${item.title.replace(/^[0-9]+_/, '')}</h3>
                <p>${snippet}</p>
            `;
            
            card.onclick = () => renderDetail(item);
            gridDiv.appendChild(card);
        });
    }

    function renderDetail(item) {
        pageTitle.textContent = item.title;
        
        let metaHtml = '';
        const metaProps = ['class', 'element', 'weakness', 'attack_type', 'hp', 'mp', 'location', 'wilayah', 'tags'];
        let hasMeta = false;
        
        metaHtml += `<div class="meta-info">`;
        metaProps.forEach(prop => {
            if (item[prop]) {
                hasMeta = true;
                metaHtml += `
                    <div class="meta-item">
                        <span class="meta-label">${prop.replace('_', ' ')}</span>
                        <span class="meta-value">${item[prop]}</span>
                    </div>
                `;
            }
        });
        metaHtml += `</div>`;
        
        if(!hasMeta) metaHtml = '';

        // Strip YAML frontmatter robustly (handling BOM and newlines)
        let cleanContent = item.content || "*Tidak ada deskripsi tersedia.*";
        cleanContent = cleanContent.replace(/^[\s\uFEFF\n]*---[\s\S]*?---[\s\n]*/, '');
        
        // Fix known encoding artifacts
        cleanContent = cleanContent.replace(/Â½/g, '½');
        cleanContent = cleanContent.replace(/ðŸ‘‰/g, '👉');
        
        const htmlContent = marked.parse(cleanContent);
        
        contentArea.innerHTML = `
            <div class="markdown-body">
                ${metaHtml}
                ${htmlContent}
            </div>
        `;
        
        window.scrollTo(0,0);
    }
});
