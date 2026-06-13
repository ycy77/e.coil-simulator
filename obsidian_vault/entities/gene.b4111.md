---
entity_id: "gene.b4111"
entity_type: "gene"
name: "proP"
source_database: "NCBI RefSeq"
source_id: "gene-b4111"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4111"
  - "proP"
---

# proP

`gene.b4111`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4111`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

proP (gene.b4111) is a gene entity. It encodes proP (protein.P0C0L7). Encoded protein function: FUNCTION: Proton symporter that senses osmotic shifts and responds by importing osmolytes such as proline, glycine betaine, stachydrine, pipecolic acid, ectoine and taurine. It is both an osmosensor and an osmoregulator which is available to participate early in the bacterial osmoregulatory response. {ECO:0000269|PubMed:10026245, ECO:0000269|PubMed:3082857, ECO:0000269|PubMed:8421314}. EcoCyc product frame: PROP-MONOMER. Genomic coordinates: 4330502-4332004. EcoCyc protein note: ProP is an osmosensing transporter which mediates the uptake of zwitterionic osmolytes such as proline and glycine betaine; ProP function protects cells from dehydration under conditions of hyperosmotic stress. The proP locus was first defined in E. coli K-12 (strain RM2 ΔputPA) by mutations which eliminate an inducible proline uptake activity and increase resistance to the toxic proline analaog, 3,4-dehydroproline . ProP mediated proline uptake is induced and stimulated by osmotic stress ; ProP has similar affinity for proline and glycine betaine . ProP catalyses active proline uptake in cytoplasmic membrane vesicles; ProP activity measured in whole cells is eliminated by the uncoupling agent CCCP and the respiration inhibitor KCN...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), lrp (protein.P0ACJ0), crp (protein.P0ACJ8), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C0L7|protein.P0C0L7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=proP; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `C` - regulator=Fis; target=proP; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=proP; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=proP; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=proP; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0013462,ECOCYC:EG11612,GeneID:948626`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4330502-4332004:+; feature_type=gene
