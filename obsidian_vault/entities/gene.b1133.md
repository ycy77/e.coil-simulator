---
entity_id: "gene.b1133"
entity_type: "gene"
name: "mnmA"
source_database: "NCBI RefSeq"
source_id: "gene-b1133"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1133"
  - "mnmA"
---

# mnmA

`gene.b1133`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1133`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mnmA (gene.b1133) is a gene entity. It encodes mnmA (protein.P25745). Encoded protein function: FUNCTION: Catalyzes the 2-thiolation of uridine at the wobble position (U34) of tRNA(Lys), tRNA(Glu) and tRNA(Gln), leading to the formation of s(2)U34, the first step of tRNA-mnm(5)s(2)U34 synthesis. Sulfur is provided by IscS, via a sulfur-relay system. Binds ATP and its substrate tRNAs. {ECO:0000269|PubMed:12549933}. EcoCyc product frame: EG11344-MONOMER. EcoCyc synonyms: asuE, ycfB, trmU. Genomic coordinates: 1192667-1193773. EcoCyc protein note: MnmA catalyzes formation of the 2-thiouridine modification of the modified nucleoside 5-methylamino-methyl-2-thiouridine (mnm5s2U34) in the wobble position of tRNAGln, tRNALys and tRNAGlu . A sulfur relay system consisting of IscS and the TusABCDE proteins is required for delivery of the sulfur atom . In vitro, a low level of MnmA activity on tRNAGlu could be achieved in the presence of Mg-ATP, cysteine, and the IscS cysteine desulfurase. The enzyme also shows activity toward anticodon stem-loop (tRNA fragment) substrates. MnmA binds to tRNALys and appears to bind to ATP . Crystal structures of MnmA together with tRNAGlu have been solved , revealing an adenylated tRNA intermediate and the basis for recognition of the specific tRNA substrates. Possible reaction mechanisms were proposed...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25745|protein.P25745]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003815,ECOCYC:EG11344,GeneID:945690`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1192667-1193773:-; feature_type=gene
