---
entity_id: "gene.b3418"
entity_type: "gene"
name: "malT"
source_database: "NCBI RefSeq"
source_id: "gene-b3418"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3418"
  - "malT"
---

# malT

`gene.b3418`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3418`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

malT (gene.b3418) is a gene entity. It encodes malT (protein.P06993). Encoded protein function: FUNCTION: Positively regulates the transcription of the maltose regulon whose gene products are responsible for uptake and catabolism of malto-oligosaccharides (PubMed:2524384, PubMed:2538630, PubMed:3305511, PubMed:7040340). Specifically binds to the promoter region of its target genes, recognizing a short DNA motif called the MalT box (5'-GGA[TG]GA-3') (PubMed:2524384, PubMed:2538630). Displays weak ATPase activity, but this activity is not required for promoter binding (PubMed:2524384). {ECO:0000269|PubMed:2524384, ECO:0000269|PubMed:2538630, ECO:0000269|PubMed:3305511, ECO:0000269|PubMed:7040340}. EcoCyc product frame: PD00237. EcoCyc synonyms: malA. Genomic coordinates: 3553085-3555790.

## Biological Role

Repressed by mlc (protein.P50456). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06993|protein.P06993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=malT; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=malT; function=+
- `represses` <-- [[protein.P50456|protein.P50456]] `RegulonDB` `S` - regulator=Mlc; target=malT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011162,ECOCYC:EG10562,GeneID:947921`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3553085-3555790:+; feature_type=gene
