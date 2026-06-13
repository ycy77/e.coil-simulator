---
entity_id: "gene.b1944"
entity_type: "gene"
name: "fliL"
source_database: "NCBI RefSeq"
source_id: "gene-b1944"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1944"
  - "fliL"
---

# fliL

`gene.b1944`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1944`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fliL (gene.b1944) is a gene entity. It encodes fliL (protein.P0ABX8). Encoded protein function: FUNCTION: Controls the rotational direction of flagella during chemotaxis. EcoCyc product frame: EG10322-MONOMER. EcoCyc synonyms: flaQI, flaAI, cheC1. Genomic coordinates: 2019618-2020082. EcoCyc protein note: fliL is the first of seven genes within the flagellar associated flaA locus (see also ). The specific function of FliL remains uncertain - recent studies in E. coli and Salmonella typhimurium, report conflicting evidence implicating FliL in motor torque generation. FliL is required for the 'motor remodeling' that is associated with swarming; FliL may act as a hub to connect and stabilize the stator (MotAB) and core basal body complexes . Single flagella motors from ΔfliL strains rotate at lower speeds and switch directions less frequently when compared to wild type and this defect is exacebated under conditions of high load; a ΔfliL strain is defective in swarming and mutant cells appear to have fractured or released filaments on swarm agar...

## Biological Role

Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02040` Flagellar assembly (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABX8|protein.P0ABX8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=fliL; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006467,ECOCYC:EG10322,GeneID:946443`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2019618-2020082:+; feature_type=gene
