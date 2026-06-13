---
entity_id: "gene.b1761"
entity_type: "gene"
name: "gdhA"
source_database: "NCBI RefSeq"
source_id: "gene-b1761"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1761"
  - "gdhA"
---

# gdhA

`gene.b1761`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1761`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gdhA (gene.b1761) is a gene entity. It encodes gdhA (protein.P00370). Encoded protein function: FUNCTION: Catalyzes the reversible oxidative deamination of glutamate to alpha-ketoglutarate and ammonia. {ECO:0000269|PubMed:235298, ECO:0000269|PubMed:241744}. EcoCyc product frame: GDHA-MONOMER. Genomic coordinates: 1842371-1843714.

## Biological Role

Repressed by spf (gene.b3864), lrp (protein.P0ACJ0), glaR (protein.P37338), nac (protein.Q47005). Activated by rpoD (protein.P00579), argP (protein.P0A8S1).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00370|protein.P00370]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=gdhA; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `C` - regulator=ArgP; target=gdhA; function=+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=gdhA; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=gdhA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=gdhA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005865,ECOCYC:EG10372,GeneID:946802`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1842371-1843714:+; feature_type=gene
