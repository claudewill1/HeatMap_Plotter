import React from 'react';

/**
 * ImageDisplay component
 * 
 * A reusable React component that displays an image inside a styled container.
 * Optionally, it shows a title above the image.
 * 
 * Props:
 *  - imageSrc (string): The source URL or base64 string of the image to display.
 *  - title (string): Optional title text to display above the image.
 */

function ImageDisplay({ imageSrc, title }) {
    if (!imageSrc) return null; // Don't render if no image source is provided
    return (
        <div className='mt-10 w-full max-w-2xl text-text'>
            {/* Display the title if provided */}
            {title && <h2 className='text-2xl font-semibold text-gray-800 mb-4'>{title}</h2>}
            {/* Render the image with styling */}
            <img
                src={imageSrc}
                alt="Generated Plot"
                className='w-full rounded-xl border shadow-md'
            />
        </div>
    )
}

export default ImageDisplay;