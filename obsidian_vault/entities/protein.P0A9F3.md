---
entity_id: "protein.P0A9F3"
entity_type: "protein"
name: "cysB"
source_database: "UniProt"
source_id: "P0A9F3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cysB b1275 JW1267"
---

# cysB

`protein.P0A9F3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9F3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: This protein is a positive regulator of gene expression for the cysteine regulon, a system of 10 or more loci involved in the biosynthesis of L-cysteine from inorganic sulfate. The inducer for CysB is N-acetylserine. CysB inhibits its own transcription. The transcription factor CysB, for "Cysteine B," is negatively autoregulated ; this regulator also controls the transcription of the operon involved in novobiocin resistance and transcription of genes involved in sulfur utilization and sulfonate-sulfur catabolism via cysteine biosynthesis and in cysteine homeostasis . A role of CysB in hydrogen peroxide was suggested , because after 10 minutes of H2O2 at 2.5 mM exposure, various target genes of CysB were found upregulated, while in the cysB knockout mutant the upregulation of them was mitigated . Nonetheless, the cysB transcription level did not show an H2O2 dose-dependent regulation . Inhibition of cysB expression by CRISPRi enhanced cellular fitness under treatment with the antibiotics carbonyl cyanide 3-chlorophenylhydrazone (CCCP) or pyocyanin . In the presence of N-acetylserine, the inducer molecule of this regulator, DNA binding by CysB tetramers to the target sequences is facilitated , but the binding to the repressor site in the cysB regulatory region is prevented . The crystal structure of CysB in complex with N-acetylserine was presented in the study by...

## Biological Role

Component of DNA-binding transcriptional dual regulator CysB (complex.ecocyc.PC00040).

## Annotation

FUNCTION: This protein is a positive regulator of gene expression for the cysteine regulon, a system of 10 or more loci involved in the biosynthesis of L-cysteine from inorganic sulfate. The inducer for CysB is N-acetylserine. CysB inhibits its own transcription.

## Outgoing Edges (18)

- `activates` --> [[gene.b0365|gene.b0365]] `RegulonDB` `S` - regulator=CysB; target=tauA; function=+
- `activates` --> [[gene.b0366|gene.b0366]] `RegulonDB` `S` - regulator=CysB; target=tauB; function=+
- `activates` --> [[gene.b0367|gene.b0367]] `RegulonDB` `S` - regulator=CysB; target=tauC; function=+
- `activates` --> [[gene.b0368|gene.b0368]] `RegulonDB` `S` - regulator=CysB; target=tauD; function=+
- `activates` --> [[gene.b1987|gene.b1987]] `RegulonDB` `S` - regulator=CysB; target=cbl; function=+
- `activates` --> [[gene.b2414|gene.b2414]] `RegulonDB` `S` - regulator=CysB; target=cysK; function=+
- `activates` --> [[gene.b2421|gene.b2421]] `RegulonDB` `S` - regulator=CysB; target=cysM; function=+
- `activates` --> [[gene.b2422|gene.b2422]] `RegulonDB` `S` - regulator=CysB; target=cysA; function=+
- `activates` --> [[gene.b2423|gene.b2423]] `RegulonDB` `S` - regulator=CysB; target=cysW; function=+
- `activates` --> [[gene.b2424|gene.b2424]] `RegulonDB` `S` - regulator=CysB; target=cysU; function=+
- `activates` --> [[gene.b2425|gene.b2425]] `RegulonDB` `S` - regulator=CysB; target=cysP; function=+
- `is_component_of` --> [[complex.ecocyc.PC00040|complex.ecocyc.PC00040]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b0933|gene.b0933]] `RegulonDB` `S` - regulator=CysB; target=ssuB; function=-
- `represses` --> [[gene.b0934|gene.b0934]] `RegulonDB` `S` - regulator=CysB; target=ssuC; function=-
- `represses` --> [[gene.b0935|gene.b0935]] `RegulonDB` `S` - regulator=CysB; target=ssuD; function=-
- `represses` --> [[gene.b0936|gene.b0936]] `RegulonDB` `S` - regulator=CysB; target=ssuA; function=-
- `represses` --> [[gene.b0937|gene.b0937]] `RegulonDB` `S` - regulator=CysB; target=ssuE; function=-
- `represses` --> [[gene.b1379|gene.b1379]] `RegulonDB` `S` - regulator=CysB; target=hslJ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1275|gene.b1275]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9F3`
- `KEGG:ecj:JW1267;eco:b1275;ecoc:C3026_07475;`
- `GeneID:93775394;945771;`
- `GO:GO:0000976; GO:0003677; GO:0003700; GO:0005829; GO:0006351; GO:0006355; GO:0010165; GO:0019344; GO:0042802`

## Notes

HTH-type transcriptional regulator CysB (Cys regulon transcriptional activator)
