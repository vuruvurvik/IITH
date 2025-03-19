import React from "react";

const Results = ({ results }) => {
    return (
        <div className="p-4">
            <h2 className="text-xl font-semibold mb-2">Search Results</h2>
            {results.length === 0 ? (
                <p>No results found.</p>
            ) : (
                <ul className="space-y-2">
                    {results.map((item, index) => (
                        <li
                            key={index}
                            className="border p-4 rounded-lg shadow-md"
                        >
                            <h3 className="text-lg font-bold">{item.title || "No Title"}</h3>
                            <p>{item.description || "No Description Available"}</p>
                            {item.link && (
                                <a
                                    href={item.link}
                                    target="_blank"
                                    rel="noopener noreferrer"
                                    className="text-blue-500"
                                >
                                    More Info
                                </a>
                            )}
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default Results;
