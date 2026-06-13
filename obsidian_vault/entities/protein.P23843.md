---
entity_id: "protein.P23843"
entity_type: "protein"
name: "oppA"
source_database: "UniProt"
source_id: "P23843"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2187863, ECO:0000269|PubMed:21983341}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "oppA b1243 JW1235"
---

# oppA

`protein.P23843`

## Static

- Type: `protein`
- Source: `UniProt:P23843`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:2187863, ECO:0000269|PubMed:21983341}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides (PubMed:2187863). Plays an important nutritional role (Probable). Binds peptides containing from two to five amino acid residues (PubMed:21983341, PubMed:3536860). Displays a preference for tripeptides and tetrapeptides over dipeptides and pentapeptides, for peptides composed of L-amino acids and for positively charged peptides (PubMed:21983341, PubMed:3536860). Cannot bind the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:2187863, ECO:0000269|PubMed:21983341, ECO:0000269|PubMed:3536860, ECO:0000305}. OppA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of oligopeptides. The crystal structure of OppA complexed with peptide ligand (modeled using a tripeptide) is highly similar to that of the well characterized S. typhimurium OppA (see ); the ligand is bound in a closed cavity deep inside the protein; the binding cavity contains large hydrated pockets believed to allow the presence of chemically diverse peptide side chains . OppA has a preference for positively charged tripeptides and tetrapeptides . A periplasmic binding protein (suggested to be OppA) purified from E. coli W binds the tripeptide Ala-Phe-Gly with a Kd of 0...

## Biological Role

Component of oligopeptide ABC transporter (complex.ecocyc.ABC-22-CPLX).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex OppABCDF involved in the uptake of oligopeptides (PubMed:2187863). Plays an important nutritional role (Probable). Binds peptides containing from two to five amino acid residues (PubMed:21983341, PubMed:3536860). Displays a preference for tripeptides and tetrapeptides over dipeptides and pentapeptides, for peptides composed of L-amino acids and for positively charged peptides (PubMed:21983341, PubMed:3536860). Cannot bind the cell wall peptide L-Ala-D-Gly-gamma-meso-diaminopimelic acid (PubMed:21705338). {ECO:0000269|PubMed:21705338, ECO:0000269|PubMed:2187863, ECO:0000269|PubMed:21983341, ECO:0000269|PubMed:3536860, ECO:0000305}.

## Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-22-CPLX|complex.ecocyc.ABC-22-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1243|gene.b1243]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23843`
- `KEGG:ecj:JW1235;eco:b1243;`
- `GeneID:945830;`
- `GO:GO:0006857; GO:0009408; GO:0015031; GO:0015833; GO:0016020; GO:0030288; GO:0055052; GO:0140205; GO:1900750; GO:1904680`

## Notes

Periplasmic oligopeptide-binding protein OppA (Polyamine-induced protein) (PI protein)
