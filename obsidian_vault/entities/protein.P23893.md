---
entity_id: "protein.P23893"
entity_type: "protein"
name: "hemL"
source_database: "UniProt"
source_id: "P23893"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemL gsa popC b0154 JW0150"
---

# hemL

`protein.P23893`

## Static

- Type: `protein`
- Source: `UniProt:P23893`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Aminomutase that catalyzes the transfer of the amine group on carbon 2 of glutamate 1-semialdehyde to the adjacent carbon 1 to form 5-aminolevulinate. {ECO:0000269|PubMed:1643048, ECO:0000269|PubMed:2045363}. Glutamate-1-semialdehyde 2,1-aminomutase (HemL) catalyzes the pyridoxal 5'-phosphate-dependent transfer of the amino group from C2 of glutamate-1-semialdehyde (GSA) to C1, thereby forming δ-aminolevulinate (ALA). ALA is the first common precursor of porphyrin biosynthesis . HemL forms a tight complex with GLUTRNAREDUCT-MONOMER, the preceding enzyme in the pathway, suggesting metabolic channeling of the highly reactive pathway intermediate GSA . Transcription of hemL is regulated by Mg2+ and PhoP . hemL mRNA contains RNA G-quadruplex (rG4) structures that appear to increase expression of hemL . hemL point mutants show leaky ALA auxotrophy . A K265R point mutant is nearly catalytically inactive . hemL belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 . An RNA G-quadruplex structure, formed by guanine-rich sequences located in the coding sequence region of the hemL gene, regulates positively the expression of the gene . PopC: "porphyrin biosynthesis" HemL: "heme biosynthesis" Review:

## Biological Role

Component of glutamate-1-semialdehyde 2,1-aminomutase (complex.ecocyc.GSAAMINOTRANS-CPLX).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Aminomutase that catalyzes the transfer of the amine group on carbon 2 of glutamate 1-semialdehyde to the adjacent carbon 1 to form 5-aminolevulinate. {ECO:0000269|PubMed:1643048, ECO:0000269|PubMed:2045363}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GSAAMINOTRANS-CPLX|complex.ecocyc.GSAAMINOTRANS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0154|gene.b0154]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P23893`
- `KEGG:ecj:JW0150;eco:b0154;ecoc:C3026_00700;`
- `GeneID:946892;`
- `GO:GO:0005829; GO:0006782; GO:0008483; GO:0030170; GO:0042286; GO:0042803`
- `EC:5.4.3.8`

## Notes

Glutamate-1-semialdehyde 2,1-aminomutase (GSA) (EC 5.4.3.8) (Glutamate-1-semialdehyde aminotransferase) (GSA-AT)
