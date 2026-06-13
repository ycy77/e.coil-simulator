---
entity_id: "protein.P06961"
entity_type: "protein"
name: "cca"
source_database: "UniProt"
source_id: "P06961"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cca b3056 JW3028"
---

# cca

`protein.P06961`

## Static

- Type: `protein`
- Source: `UniProt:P06961`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the addition and repair of the essential 3'-terminal CCA sequence in tRNAs without using a nucleic acid template (PubMed:3516995). Adds these three nucleotides in the order of C, C, and A to the tRNA nucleotide-73, using CTP and ATP as substrates and producing inorganic pyrophosphate (PubMed:3516995). tRNA 3'-terminal CCA addition is required both for tRNA processing and repair (PubMed:22076379). Also involved in tRNA surveillance by mediating tandem CCA addition to generate a CCACCA at the 3' terminus of unstable tRNAs (PubMed:22076379). While stable tRNAs receive only 3'-terminal CCA, unstable tRNAs are marked with CCACCA and rapidly degraded (PubMed:22076379). The structural flexibility of RNA controls the choice between CCA versus CCACCA addition: following the first CCA addition cycle, nucleotide-binding to the active site triggers a clockwise screw motion, producing torque on the RNA (By similarity). This ejects stable RNAs, whereas unstable RNAs are refolded while bound to the enzyme and subjected to a second CCA catalytic cycle (By similarity). Also shows highest phosphatase activity in the presence of Ni(2+) and hydrolyzes pyrophosphate, canonical 5'-nucleoside tri- and diphosphates, NADP, and 2'-AMP with the production of Pi (PubMed:15210699)...

## Biological Role

Catalyzes TRNA-CYTIDYLYLTRANSFERASE-RXN (reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

FUNCTION: Catalyzes the addition and repair of the essential 3'-terminal CCA sequence in tRNAs without using a nucleic acid template (PubMed:3516995). Adds these three nucleotides in the order of C, C, and A to the tRNA nucleotide-73, using CTP and ATP as substrates and producing inorganic pyrophosphate (PubMed:3516995). tRNA 3'-terminal CCA addition is required both for tRNA processing and repair (PubMed:22076379). Also involved in tRNA surveillance by mediating tandem CCA addition to generate a CCACCA at the 3' terminus of unstable tRNAs (PubMed:22076379). While stable tRNAs receive only 3'-terminal CCA, unstable tRNAs are marked with CCACCA and rapidly degraded (PubMed:22076379). The structural flexibility of RNA controls the choice between CCA versus CCACCA addition: following the first CCA addition cycle, nucleotide-binding to the active site triggers a clockwise screw motion, producing torque on the RNA (By similarity). This ejects stable RNAs, whereas unstable RNAs are refolded while bound to the enzyme and subjected to a second CCA catalytic cycle (By similarity). Also shows highest phosphatase activity in the presence of Ni(2+) and hydrolyzes pyrophosphate, canonical 5'-nucleoside tri- and diphosphates, NADP, and 2'-AMP with the production of Pi (PubMed:15210699). Displays a metal-independent phosphodiesterase activity toward 2',3'-cAMP, 2',3'-cGMP, and 2',3'-cCMP (PubMed:15210699). Without metal or in the presence of Mg(2+), this protein hydrolyzes 2',3'-cyclic substrates with the formation of 2'-nucleotides, whereas in the presence of Ni(2+), it also produces some 3'-nucleotides (PubMed:15210699). These phosphohydrolase activities are probably involved in the repair of the tRNA 3'-CCA terminus degraded by intracellular RNases (PubMed:15210699). {ECO:0000250|UniProtKB:O28126, ECO:0000269|PubMed:15210699, ECO:0000269|PubMed:22076379, ECO:0000269|PubMed:3516995}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN|reaction.ecocyc.TRNA-CYTIDYLYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3056|gene.b3056]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P06961`
- `KEGG:ecj:JW3028;eco:b3056;ecoc:C3026_16700;`
- `GeneID:947553;`
- `GO:GO:0000049; GO:0000287; GO:0001680; GO:0004112; GO:0004810; GO:0005524; GO:0016791; GO:0042245; GO:0106354; GO:0160016`
- `EC:2.7.7.72; 3.1.3.-; 3.1.4.-`

## Notes

Multifunctional CCA protein [Includes: CCA-adding enzyme (EC 2.7.7.72) (CCA tRNA nucleotidyltransferase) (tRNA CCA-pyrophosphorylase) (tRNA adenylyl-/cytidylyl-transferase) (tRNA nucleotidyltransferase) (tRNA-NT); 2'-nucleotidase (EC 3.1.3.-); 2',3'-cyclic phosphodiesterase (EC 3.1.4.-); Phosphatase (EC 3.1.3.-)]
