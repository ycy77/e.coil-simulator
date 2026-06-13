---
entity_id: "gene.b2703"
entity_type: "gene"
name: "srlE"
source_database: "NCBI RefSeq"
source_id: "gene-b2703"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2703"
  - "srlE"
---

# srlE

`gene.b2703`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2703`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

srlE (gene.b2703) is a gene entity. It encodes srlE (protein.P56580). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. EcoCyc product frame: GUTA-MONOMER. EcoCyc synonyms: sbl, gutA, gutE, srlA, srlA-2. Genomic coordinates: 2826392-2827351. EcoCyc protein note: Contains PTS Enzyme IIB and IIC1 (IIC-C) domain. The IIB domain is largely hydrophilic and contains a cysteine residue at position 71 which may be the second phosphorylation site .

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P56580|protein.P56580]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=srlE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008892,ECOCYC:EG10969,GeneID:948933`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2826392-2827351:+; feature_type=gene
