import React from "react";

const SearchBar = ({ query, setQuery, onSearch }) => {
    return (
        <div className="flex items-center space-x-4 p-4">
            <input
                type="text"
                placeholder="Search for disasters (e.g., earthquakes, floods)..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                className="p-2 border border-gray-300 rounded-lg w-full"
            />
            <button
                onClick={onSearch}
                className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
            >
                Search
            </button>
        </div>
    );
};

export default SearchBar;
