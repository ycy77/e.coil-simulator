---
entity_id: "gene.b3405"
entity_type: "gene"
name: "ompR"
source_database: "NCBI RefSeq"
source_id: "gene-b3405"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3405"
  - "ompR"
---

# ompR

`gene.b3405`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3405`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompR (gene.b3405) is a gene entity. It encodes ompR (protein.P0AA16). Encoded protein function: FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:3010044, PubMed:3536870). Plays a central role in both acid and osmotic stress responses (PubMed:28526842, PubMed:30524381). Binds AT-rich DNA (PubMed:10633113). Binds to the promoter of both ompC and ompF; at low osmolarity it activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:2403550, PubMed:2557454, PubMed:3023382, PubMed:3533941, PubMed:7592927). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation (PubMed:29138484). Phosphorylated by EnvZ; this stimulates OmpR's DNA-binding ability (PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113, PubMed:7934854). Is also dephosphorylated by EnvZ (PubMed:2558046, PubMed:2668281, PubMed:7934854). A single OmpR protein can bind to DNA; OmpR dimers can form on the DNA in either direction, suggesting that interactions between the 2 DNA-binding domains are weak or absent (PubMed:18195018)...

## Biological Role

Repressed by omrA (gene.b4444), omrB (gene.b4445), crp (protein.P0ACJ8), nac (protein.Q47005). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA16|protein.P0AA16]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ompR; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=ompR; function=-+
- `represses` <-- [[gene.b4444|gene.b4444]] `RegulonDB` `S` - regulator=OmrA; target=ompR; function=-
- `represses` <-- [[gene.b4445|gene.b4445]] `RegulonDB` `S` - regulator=OmrB; target=ompR; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=ompR; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ompR; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011110,ECOCYC:EG10672,GeneID:947913`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3535865-3536584:-; feature_type=gene
