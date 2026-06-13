---
entity_id: "protein.P0ADE4"
entity_type: "protein"
name: "tamA"
source_database: "UniProt"
source_id: "P0ADE4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795, ECO:0000269|PubMed:17214547, ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:24056943, ECO:0000269|PubMed:25341963}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tamA yftM ytfM b4220 JW4179"
---

# tamA

`protein.P0ADE4`

## Static

- Type: `protein`
- Source: `UniProt:P0ADE4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795, ECO:0000269|PubMed:17214547, ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:24056943, ECO:0000269|PubMed:25341963}.

## Enriched Summary

FUNCTION: Component of the translocation and assembly module (TAM), which facilitates the insertion and assembly of specific beta-barrel proteins into the outer membrane (PubMed:22466966, PubMed:25341963, PubMed:28752534, PubMed:39174534). Promotes the assembly and secretion across the outer membrane of a subset of autotransporters, such as Ag43 (PubMed:22466966, PubMed:25341963). Involved in the assembly of the outer membrane usher protein FimD (PubMed:28752534). In vitro, when TAM is reconstituted into preformed liposomes, it can promote the assembly of several outer membrane proteins, including OmpA, EspP, Ag43 and FadL (PubMed:39174534). TamA is sufficient to catalyze a low level of outer membrane protein (OMP) assembly, but both TamA and TamB are required for efficient OMP assembly (PubMed:39174534). TamA must bind to the beta signal of client proteins to promote their assembly (PubMed:39174534). Has anion selective channel-forming ability, but the physiological relevance of this activity is unclear (PubMed:17214547). {ECO:0000269|PubMed:17214547, ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:25341963, ECO:0000269|PubMed:28752534, ECO:0000269|PubMed:39174534}. TamA, a member of the Omp85 superfamily , localizes to the outer membrane in E. coli K-12 . TamA forms a complex (the translocation and assembly module or TAM) with the inner membrane protein, TamB...

## Biological Role

Component of translocation and assembly module (complex.ecocyc.CPLX0-7976).

## Annotation

FUNCTION: Component of the translocation and assembly module (TAM), which facilitates the insertion and assembly of specific beta-barrel proteins into the outer membrane (PubMed:22466966, PubMed:25341963, PubMed:28752534, PubMed:39174534). Promotes the assembly and secretion across the outer membrane of a subset of autotransporters, such as Ag43 (PubMed:22466966, PubMed:25341963). Involved in the assembly of the outer membrane usher protein FimD (PubMed:28752534). In vitro, when TAM is reconstituted into preformed liposomes, it can promote the assembly of several outer membrane proteins, including OmpA, EspP, Ag43 and FadL (PubMed:39174534). TamA is sufficient to catalyze a low level of outer membrane protein (OMP) assembly, but both TamA and TamB are required for efficient OMP assembly (PubMed:39174534). TamA must bind to the beta signal of client proteins to promote their assembly (PubMed:39174534). Has anion selective channel-forming ability, but the physiological relevance of this activity is unclear (PubMed:17214547). {ECO:0000269|PubMed:17214547, ECO:0000269|PubMed:22466966, ECO:0000269|PubMed:25341963, ECO:0000269|PubMed:28752534, ECO:0000269|PubMed:39174534}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7976|complex.ecocyc.CPLX0-7976]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4220|gene.b4220]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADE4`
- `KEGG:ecj:JW4179;eco:b4220;ecoc:C3026_22795;`
- `GeneID:75202460;948733;`
- `GO:GO:0005886; GO:0009279; GO:0009306; GO:0089705; GO:0097347`

## Notes

Translocation and assembly module subunit TamA (Autotransporter assembly factor TamA)
