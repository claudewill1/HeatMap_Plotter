import matplotlib.pyplot as plt
import numpy as np

def read_and_plot_data(file_path: str) -> dict:
    """
    Read table data from file and create plot.
    -Open file and read lines.
    - Parse into x, y, z arrays.
    - Call generate_colormap_plot
    - Return path to generated image or base64 string.
    - Handle exceptions and errors.
    """
    try:
        # Open file using a reader or pandas
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Parse the lines into x, y, z lists/arrays
        x, y, z = [], [], []
        # Call generate_colormap_plot with parsed data
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 3:
                x.append(float(parts[0]))
                y.append(float(parts[1]))
                z.append(float(parts[2]))
        # Return generated image path
        image_path = generate_colormap_plot(x, y, z)
        return {"image_path": image_path}
    except Exception as e:
        raise Exception(f"Error reading and plotting data: {str(e)}")
    

def generate_colormap_plot(x: list, y: list, z: list, output_path="output_plot.png"):
        """
        Plot 2D scatter or colormap using matplotlib.
        - Create figure and axis.
        - Use scatter or tricontourf for color mapping.
        - Add colorbar.
        - Set labels and title.
        - Save figure to file.
        - Close figure.
        - Return path to saved image.
        """
        try:
            # Create matplotlib figure and axis
            fig, ax = plt.subplots()
            # Use scatter or trincontourf for x, y, c=z
            if len(x) == len(y) == len(z):
                scatter = ax.scatter(x, y, c=z, cmap='viridis', edgecolor='k')
            else:
                raise ValueError("x, y, and z must have the same length")
            # Add colorbar and labels
            cbar = plt.colorbar(scatter, ax=ax)
            cbar.set_label('Color Scale')
            ax.set_xlabel('X-axis Label')
            ax.set_ylabel('Y-axis Label')
            ax.set_title('Colormap Plot')
            # Adjust layout and save figure
            plt.tight_layout()
            fig.savefig(output_path)
            # Close figure and release memory
            plt.close(fig)
            # Return saved image path
            return output_path    
        except Exception as e:
            raise Exception(f"Error generating colormap plot: {str(e)}")
        