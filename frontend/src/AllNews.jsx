import { use, useEffect, useState } from 'react';
import { io } from 'socket.io-client'
import './AllNews.css';
function AllNews() {
    const [news, setNews] = useState([]);
    const [currentPage, setCurrentPage] = useState(1);
    const [newsPerPage, setNewsPerPage] = useState(6);
    const [searchTerm, setSearchTerm] = useState('');
    const [filteredNews, setFilteredNews] = useState([]);

    useEffect(() => {
        const socket = io('localhost:5000');
        socket.on('connect', () => {
            console.log('Connected to the server');
            socket.emit('getAllNews'); // Request all news when connected
        });
        socket.on('allNews', (news) => {
            console.log('Received all news:', news.news);
            setNews(news.news);
        });
        setInterval(() => {
            socket.emit('getAllNews'); // Request all news periodically
        }, 100000); // Every 100 seconds

        // Cleanup function to disconnect the socket when the component unmounts
        return () => {
            socket.disconnect();
        }
    }, []);

    useEffect(() => {
        const footer = document.querySelector('footer');
        if (footer) {
            footer.style.position = '';
            footer.style.bottom = '0';
            footer.style.width = '100%';
        }
    }, []);

    const lastItemIndex = currentPage * newsPerPage;
    const firstItemIndex = lastItemIndex - newsPerPage;
    const currentNews = news.slice(firstItemIndex, lastItemIndex);

    const pages = Math.ceil(news.length / newsPerPage);
    const pageNumbers = Array.from({ length: pages }, (_, index) => index + 1);

    const handlePageChange = (pageNumber) => {
        setCurrentPage(pageNumber);
    };

  return (
    <>
    <div classname="search-bar">
            <div className='search-bar'>
        <input
            type="text"
            placeholder="Search news..."
            value={searchTerm}
            onChange={(e) => {
                setSearchTerm(e.target.value);
                const filtered = news.filter(item =>
                    item.name.toLowerCase().includes(e.target.value.toLowerCase())
                );
                setFilteredNews(filtered);
            }}
        />
    </div>
        {searchTerm.length < 1 ? (<>
    <div className="all-news-div">
        {currentNews.length > 0 ? (
            currentNews.map((item) => (
            <ul>
                <li key={item.name} className="news-item">
                    <h2><a href={item.link} target="_blank" rel="noopener noreferrer">{item.name}</a></h2>
                </li>
            </ul>
            ))
        ) : (
            <p>Loading....</p>
        )}
    </div>
    <div className="pagination">
            {pageNumbers.map((number) => (
            <button
                key={number}
                onClick={() => handlePageChange(number)}
                className={currentPage === number ? 'active' : ''}
            >
                {number}
            </button>
            ))}
    </div>
    </>
    ) : (
        <div className="search-results">
            {news.filter(item => item.name.toLowerCase().includes(searchTerm.toLowerCase())).map((item) => (
                <ul key={item.name}>
                    <li className="news-item">
                        <h2><a href={item.link} target="_blank" rel="noopener noreferrer">{item.name}</a></h2>
                    </li>
                </ul>
            ))}
        </div>
    )
    }
    </div>
    </>
  );
}
export default AllNews;



