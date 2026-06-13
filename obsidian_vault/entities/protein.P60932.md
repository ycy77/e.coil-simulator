---
entity_id: "protein.P60932"
entity_type: "protein"
name: "uppP"
source_database: "UniProt"
source_id: "P60932"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15138271, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15138271, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "uppP bacA upk b3057 JW3029"
---

# uppP

`protein.P60932`

## Static

- Type: `protein`
- Source: `UniProt:P60932`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15138271, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15138271, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Catalyzes the dephosphorylation of undecaprenyl diphosphate (UPP). Confers resistance to bacitracin. {ECO:0000269|PubMed:15778224}. The purified BacA protein has undecaprenyl pyrophosphate (Und-PP or C55-PP) phosphatase activity, but not undecaprenol phosphokinase activity . The bacA gene product is not essential for growth, but the product of the BacA catalysed reaction, undecaprenyl phosphate, is essential for the synthesis of peptidoglycan and other cell wall components. At least three additional gene products, G6439-MONOMER "YbjG", PGPPHOSPHAB-MONOMER "PgpB", and G7146-MONOMER "LpxT", are thought to have undecaprenyl pyrophosphate phosphatase activity in E. coli . BacA accounts for approximately three quarters of the total C55-PP phosphatase activity . BacA catalyses C55-PP dephosphorylation on the periplasmic side of the inner membrane . Purified BacA dephosphorylates farnesyl pyrophosphate (FPP); the optimal pH for this assay is 6.5-7 and the enzyme requires Mg2+ or Ca2+ for activity; bacitracin inhibits the dephosphorylation of FPP by BacA BacA is predicted to contain 8 transmembrane helices with the N and C-termini located in the cytoplasm; two conserved motifs - region I and region II - and a conserved histidine residue (His-30) are thought to form the catalytic core of the enzyme...

## Biological Role

Catalyzes RXN-11776 (reaction.ecocyc.RXN-11776), UNDECAPRENYL-DIPHOSPHATASE-RXN (reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

FUNCTION: Catalyzes the dephosphorylation of undecaprenyl diphosphate (UPP). Confers resistance to bacitracin. {ECO:0000269|PubMed:15778224}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11776|reaction.ecocyc.RXN-11776]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN|reaction.ecocyc.UNDECAPRENYL-DIPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3057|gene.b3057]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60932`
- `KEGG:ecj:JW3029;eco:b3057;ecoc:C3026_16705;`
- `GeneID:947551;`
- `GO:GO:0000270; GO:0005886; GO:0008360; GO:0009252; GO:0016462; GO:0046677; GO:0050380; GO:0071555`
- `EC:3.6.1.27`

## Notes

Undecaprenyl-diphosphatase (EC 3.6.1.27) (Bacitracin resistance protein) (Undecaprenyl pyrophosphate phosphatase)
