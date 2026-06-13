---
entity_id: "gene.b0937"
entity_type: "gene"
name: "ssuE"
source_database: "NCBI RefSeq"
source_id: "gene-b0937"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0937"
  - "ssuE"
---

# ssuE

`gene.b0937`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0937`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ssuE (gene.b0937) is a gene entity. It encodes ssuE (protein.P80644). Encoded protein function: FUNCTION: Catalyzes an NADPH-dependent reduction of FMN, but is also able to reduce FAD or riboflavin. EcoCyc product frame: MONOMER0-146. EcoCyc synonyms: ssi4, ycbP. Genomic coordinates: 996937-997512. EcoCyc protein note: The SsuE protein is an NAD(P)H-dependent FMN reductase that provides FMNH2 for SsuD, an FMNH2-dependent monooxygenase . FMN is the preferred flavin substrate of SsuE, but the enzyme is also active with FAD and riboflavin . Rapid reaction kinetic analysis was performed to investigate the reductive half-reaction by SsuE . The presence of SsuD and the octanesulfonate substrate changes the kinetics of FMN reduction catalyzed by SsuE . Further studies showed the formation of a stable complex between SsuD and SsuE, which changes the flavin environment of FMN-bound SsuE . These results support a model for direct transfer of the reduced flavin from SsuE to SsuD. SsuE belongs to the flavodoxin-like superfamily. Crystal structures of SsuE in the apo, FMN-bound, and FMNH2-bound forms have been solved . SsuE forms a dimer of dimers in the crystal structure; in solution, the protein is in a dimer-tetramer equilibrium that depends on the presence of FMN...

## Biological Role

Repressed by cysB (protein.P0A9F3), nac (protein.Q47005). Activated by rpoD (protein.P00579), cbl (protein.Q47083).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P80644|protein.P80644]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ssuE; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=ssuE; function=+
- `represses` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=ssuE; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ssuE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003182,ECOCYC:G6479,GeneID:945947`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:996937-997512:-; feature_type=gene
