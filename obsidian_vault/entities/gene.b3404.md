---
entity_id: "gene.b3404"
entity_type: "gene"
name: "envZ"
source_database: "NCBI RefSeq"
source_id: "gene-b3404"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3404"
  - "envZ"
---

# envZ

`gene.b3404`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3404`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

envZ (gene.b3404) is a gene entity. It encodes envZ (protein.P0AEJ4). Encoded protein function: FUNCTION: Member of the two-component regulatory system EnvZ/OmpR involved in osmoregulation (particularly of genes ompF and ompC) as well as other genes (PubMed:2997120, PubMed:3536870). EnvZ functions as a membrane-associated protein kinase that phosphorylates OmpR in response to environmental signals; at low osmolarity OmpR activates ompF transcription, while at high osmolarity it represses ompF and activates ompC transcription (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2656684, PubMed:2668281, PubMed:2668953, PubMed:2674113). Also dephosphorylates OmpR in the presence of ATP (PubMed:1323560, PubMed:2277041, PubMed:2558046, PubMed:2668281). The cytoplasmic dimerization domain (CDD) forms an osmosensitive core; increasing osmolarity stabilizes this segment (possibly by its contraction), enhancing the autophosphorylation rate and consequently, downstream phosphotransfer to OmpR and signaling (PubMed:22543870, PubMed:28256224). Autophosphorylation is greater when full-length EnvZ is reconstituted in a lipid environment, lipid-mediated allostery impacts the kinase function of EnvZ (PubMed:28256224). Involved in acid stress response; this requires EnvZ but not OmpR phosphorylation, and suggests that EnvZ senses cytoplasmic acidic pH (PubMed:29138484)...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEJ4|protein.P0AEJ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=envZ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=envZ; function=-+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=envZ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011108,ECOCYC:EG10269,GeneID:947272`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3534516-3535868:-; feature_type=gene
