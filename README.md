# Signalgrundlag

- **Lecture specific files**: files/* – `En mappe med filer til øvelser og eksempler fra undervisningen.`

---

## Forberedelse til lektionen

Følg denne guide nøje for at være klar til undervisningen:

### 1. Literatur

**Primær litteratur:**

- [Data Wrangling with Python af Jacek Gołębiewski (PDF)](https://datawranglingpy.gagolewski.com/datawranglingpy.pdf)
  - Kapitel 3.1, 5.1, 5.3 : Tidsserie og signal analyse
  - Kapitel 5.2.2, 5.4: Slicing and indexing
- GDPR
  - Artikel 4: Definitioner relateret til persondata og behandling
  - Artikel 6: Lovlig behandling af persondata
  - Artikel 7: Gyldigt samtykke
  - Artikel 9: Behandling af særlige kategorier af persondata (herunder sundhedsdata)
  - Artikel 17: Retten til at blive glemt

**Supplerende litteratur:**
- [NumPy Documentation](https://numpy.org/doc/)
  - https://numpy.org/doc/2.4/reference/arrays.ndarray.html
  - https://numpy.org/doc/2.4/reference/generated/numpy.genfromtxt.html
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
  - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
  - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html
  - https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html

**Exercise Video:**
- [HeartCycleExtractor Exercise Video](https://panopto.aau.dk/Panopto/Pages/Viewer.aspx?id=28ed6727-214f-40fa-84cd-b3fe00d09eda)

**Til Flowcharts of class diagrammer:**  
Her er der 2 muligheder. Jeg bruger personligt `Mermaid` idag. 
Men jeg startede med `DrawIO` hjemmesiden.
- [Mermaid (https://mermaid.live)](https://mermaid.live)
  - [Flowcharts](https://mermaid.js.org/syntax/flowchart.html)
  - [Class Diagrams](https://mermaid.js.org/syntax/classDiagram.html)
- [Draw IO (https://draw.io)](https://app.diagrams.net/)

---

### 2. Installationer og opsætning
- Sørg for at Python og VS Code er installeret (se evt. tidligere guides).
- Tjek at du har følgende extensions i Visual Studio Code:
  - `Python`
  - `jupyter`


- Download eller opdater materialet:
> ```zsh
> git clone https://github.com/AAU-ST2-Programming/signals_1.git
> cd signals_1
> git pull
> ```

---

## Lektionens fokus

- Grundlæggende signalbehandling i Python
- NumPy arrays og operationer
- Læsning af signaldata fra filer
- Visualisering af signaler med matplotlib

---

## Forventninger til forberedelse og undervisning

- **Før/efter kursusgang:**
  - Gennemgå tidligere kursusgange og kodeeksempler
  - Læs nyt materiale som beskrevet ovenfor
- **Tidsforbrug:**
  - 4 timers forberedelse (hjemme, før undervisning)
  - 4 timers undervisning og gruppeopgaver
  - 4 timers individuel opgaveregning (hjemme, efter undervisning)

---

## Spørgsmål og opgaver

- Til hver opgave i undervisningen vil der være:
  - En opgavebeskrivelse
  - En guide til hvordan opgaven løses
  - Svar på opgaven
- Opgaverne bygger videre på hinanden og bliver gradvist sværere.
- Til eksamen vil der kun være en opgavebeskrivelse – du skal selv kunne vurdere, hvordan opgaven løses.

---

**Husk:** Brug "Data Wrangling with Python" som din primære kilde til signalbehandling!
