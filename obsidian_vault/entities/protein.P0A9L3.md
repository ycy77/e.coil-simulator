---
entity_id: "protein.P0A9L3"
entity_type: "protein"
name: "fklB"
source_database: "UniProt"
source_id: "P0A9L3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm. Periplasm {ECO:0000269|PubMed:7610040, ECO:0000269|PubMed:8703024}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fklB ytfC b4207 JW5746"
---

# fklB

`protein.P0A9L3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9L3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm. Periplasm {ECO:0000269|PubMed:7610040, ECO:0000269|PubMed:8703024}.

## Enriched Summary

FUNCTION: PPIases accelerate the folding of proteins (Probable). Catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:8703024). Displays a preference for substrates with a lysyl residue in the P1 position (PubMed:8703024). {ECO:0000269|PubMed:8703024, ECO:0000305}. The FklB protein is an FKBP (FK506 binding protein)-type peptidyl-prolyl cis-trans isomerase (PPIase) that may be located in the periplasm. Sequence analysis indicates that FklB is related to the Mip (macrophage infectivity potentiator)-like FKBPs which occur in many intracellular pathogens . Substrates were identified by pull-down assay and include Rob, Crl, PcnB, and ObgE . Purified FklB (from E. coli K-12 HB101) is a dimer in solution; the enzyme shows a preference for substrate with a hydrophobic side chain in position P1 (eg Suc-Ala-Leu-Pro-Phe) and also for a lysyl residue at this position (Suc-Ala-Lys-Pro-Phe); PPIase activity is inhibited in vitro by the immunosuppressive drug FK506 . Based on sequence similarity, FklB appears to have a domain structure consisting of an N-terminal dimerization domain, a long α-helix linker, and a C-terminal domain that is implicated in binding FK506 and rapamycin . Mutations in the linker helix affect the chaperone activity, structure and stability of FklB, but have little effect on rapamycin binding...

## Biological Role

Component of peptidyl-prolyl cis-trans isomerase FklB (complex.ecocyc.CPLX0-3924).

## Annotation

FUNCTION: PPIases accelerate the folding of proteins (Probable). Catalyzes the cis-trans isomerization of proline imidic peptide bonds in oligopeptides (PubMed:8703024). Displays a preference for substrates with a lysyl residue in the P1 position (PubMed:8703024). {ECO:0000269|PubMed:8703024, ECO:0000305}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3924|complex.ecocyc.CPLX0-3924]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4207|gene.b4207]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9L3`
- `KEGG:ecj:JW5746;eco:b4207;ecoc:C3026_22725;`
- `GeneID:93777614;948726;`
- `GO:GO:0003755; GO:0005528; GO:0005829; GO:0006457; GO:0042597; GO:0042802; GO:0042803`
- `EC:5.2.1.8`

## Notes

FKBP-type 22 kDa peptidyl-prolyl cis-trans isomerase (FKBP22) (PPIase) (EC 5.2.1.8) (Rotamase)
