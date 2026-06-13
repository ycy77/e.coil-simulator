---
entity_id: "gene.b0592"
entity_type: "gene"
name: "fepB"
source_database: "NCBI RefSeq"
source_id: "gene-b0592"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0592"
  - "fepB"
---

# fepB

`gene.b0592`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0592`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fepB (gene.b0592) is a gene entity. It encodes fepB (protein.P0AEL6). Encoded protein function: FUNCTION: Part of the ABC transporter complex FepBDGC involved in ferric enterobactin uptake (PubMed:3011753). Binds ferric enterobactin (PubMed:10986237, PubMed:25173704, PubMed:7551033). Can also bind ferric enantioenterobactin, the left-handed stereoisomer of the natural E.coli siderophore, and the apo-siderophore, enterobactin, but does not bind ferric agrobactin (PubMed:10986237). {ECO:0000269|PubMed:10986237, ECO:0000269|PubMed:25173704, ECO:0000269|PubMed:3011753, ECO:0000269|PubMed:7551033}. EcoCyc product frame: FEPB-MONOMER. Genomic coordinates: 623554-624510. EcoCyc protein note: FepB is the periplasmic binding protein of a ferric enterobactin ABC transport system. Purified FepB binds ferric enterobactin and enterobactin with high affinity (Kd = 30nM and 60nM respectively). Varying the periplasmic concentration of FepB does not affect the rate of uptake of labeled ferric enterobactin suggesting that the rate limiting step in ferric enterobactin uptake is transport across the outer membrane. FepB is synthesized at relatively low levels - approximately 3800 molecules per cell . Solution structures of FepB with and without bound gallium enterobactin suggest that ligand binding does not induce large conformational changes...

## Biological Role

Repressed by fur (protein.P0A9A9), rutR (protein.P0ACU2). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEL6|protein.P0AEL6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fepB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fepB; function=-
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `S` - regulator=RutR; target=fepB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002038,ECOCYC:EG10294,GeneID:947538`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:623554-624510:-; feature_type=gene
