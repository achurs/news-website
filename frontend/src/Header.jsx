import {Link} from 'react-router-dom';
import './Header.css';
function Header(){
    return (
        <header className="header">
            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>
                    <li>
                        <Link to="/all">All News</Link>
                    </li>
                    <li>
                        <Link to="/chatbot">Chatbot</Link>
                    </li>
                </ul>
            </nav>
        </header>
    );
}

export default Header;
