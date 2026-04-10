<h1>Maze Solver</h1>

<p>A visual maze generator and solver built with Python and Tkinter, based on the <a href="https:boot.dev">Boot.dev</a> guided project.</p>

<h2>Features</h2>

<h3>Core (Guided Project)</h3>

<ul>
    <li>Procedural maze generation using recursive backtracking</li>
    <li>Depth-first search solver with animated path visualization</li>
    <li>Undo path drawing when a dead end is reached</li>
</ul>

<h3>Added UI Enhancements</h3>

</h4>Interactive Controls</h4>

<ul>
    <li>Row and Column inputs -- Entry fields allow the user to specify maze dimensions before generation</li>
    <li>Submit button -- Triggers maze generation with the provided dimensions; the solved maze remains visible until a new one is requested</li>
    <li>Maze-only canvas clearing on resubmit, preserving all UI widgets using canvas draw tags</li>
</ul>

<h4>Dynamic Centering</h4>

<p>Rather than using a fixed cell size and margin, the maze grid is calculated to fill the available window space and remain centered regardless of the row/column count provided.</p>

<p>The algorithm:</p>

<ol>
    <li>Derives the usable grid area by subtracting fixed side and top/bottom margins from the window dimensions</li>
    <li>Calculates the maximum cell size that fits within that area given the requested row/column count</li>
    <li>Computes the window center and grid center, then subtracts to find the top-left origin of cell (0, 0)</li>
</ol>

<p>This ensures the maze always appears visually balanced in the window, whether the user requests a 5x5 or a 40x40 grid.</p>

<h2>Running the Project</h2>

<code>python main.py</code>

<p>Enter the desired number of rows and columns, then click Submit to generate and solve a new maze.</p>

<h3>Requirements</h3>

<ul>
    <li>Python 3.x</li>
    <li>Tkinter (included in the standard library)</li>
</ul>