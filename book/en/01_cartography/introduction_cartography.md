# Introduction to Geological Mapping

```{admonition} Learning Objectives
:class: important

By the end of this chapter, you will be able to:
1. Understand the importance of geological mapping in Earth Sciences.
2. Identify and measure the spatial orientation of geological planes (strike, dip direction, and dip).
3. Interpret basic symbology on a geological map.
4. Solve simple conceptual problems regarding the spatial disposition of terrain.
```

---

## 1. What is a Geological Map?

A **geological map** is a two-dimensional, scaled representation of the spatial distribution of different rock units (or sediments) outcropping on the Earth's surface, as well as the geological structures that affect them (folds, faults, unconformities).

Unlike a conventional topographic map, a geological map provides a projection of the **third dimension** into the subsurface by interpreting the geometry of contact lines.

---

## 2. Plane Orientation: Strike, Dip, and Dip Direction

To structurally characterize any geological plane (such as a rock layer or a fault), three angular parameters measured with a geologist's compass are used:

*   **Strike (Trend of the layer):** The horizontal angle between magnetic north and the line of intersection of the geological plane with a virtual horizontal plane.
*   **Dip (Inclination):** The angle of maximum slope measured vertically between the horizontal plane and the geological plane. It ranges between $0^\circ$ (horizontal) and $90^\circ$ (vertical).
*   **Dip Direction (Sense of inclination):** The direction of the horizontal projection of the line of maximum slope. It is always perpendicular to the strike ($90^\circ$ to the right or left).

### Mathematical Relationship of Apparent Dip

If inclination is measured in a direction that is not perpendicular to the strike, an **apparent dip** ($\alpha$) is obtained, which is always less than or equal to the **true dip** ($\beta$). The mathematical relationship is given by:

$$
\tan(\alpha) = \tan(\beta) \cdot \sin(\theta)
$$

Where:
*   $\alpha$ is the apparent dip.
*   $\beta$ is the true dip.
*   $\theta$ is the horizontal angle between the strike direction and the direction in which the apparent dip is measured.

---

## 3. Types of Geological Contacts

The geometric relationship between different rock units defines the type of contact. The most common contact relationships are outlined below:

As shown in {numref}`fig-diagram-01-cartography-introduction-cartography-01`, the diagram is versioned as a static image.

```{figure} ../../_static/generated/diagrams/en/01_cartography_introduction_cartography_01.svg
:name: fig-diagram-01-cartography-introduction-cartography-01
:alt: Diagram generated from code
:width: 90%
:align: center

Diagram generated from code.
```

---

## 4. The "V" Rule in Mapping

One of the fundamental rules for interpreting the spatial layout of layers from their surface exposure is the **V Rule**:

> *When an inclined layer crosses a topographic valley, the trace of its contact draws a **V** shape whose apex points in the direction of the dip of the plane (with minor exceptions where the valley slope is greater than the dip).*

*   **Horizontal Beds:** Contact traces are parallel to topographic contour lines.
*   **Vertical Beds:** Contact traces are represented as straight lines on the map, completely ignoring the terrain's topography.

---

## 5. Self-Assessment Exercises

```{admonition} Conceptual Question: Apparent Dip
:class: tip, dropdown

**Question:** If a layer has a true dip of $30^\circ$ towards the East, what will be its apparent dip if we observe it in a terrain cut oriented exactly in a North-South direction?

**Solution:**
Since the dip direction is East, the strike of the layer is North-South (perpendicular to East). The direction of observation (North-South) is parallel to the strike of the layer.
The angle $\theta$ between the strike direction and the direction of observation is $0^\circ$.

Applying the formula:
$$
\tan(\alpha) = \tan(30^\circ) \cdot \sin(0^\circ) = 0 \implies \alpha = 0^\circ
$$

Therefore, on a cross-section plane parallel to the strike, the bed will appear completely horizontal (apparent dip of $0^\circ$).
```

---

## 6. Future Practical Exercises Battery

In upcoming updates to this interactive book, computational tools and executable Python notebooks will be incorporated to solve:

1.  **Three-point problem:** Calculation of the strike and dip of a plane from three known elevations.
2.  **Geological Cross-Section Generation:** Automated construction of cross-sections from topographic profiles and map traces.
3.  **Structure contours:** Automatic tracing of contacts using spatial interpolation.
