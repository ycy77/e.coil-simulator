---
entity_id: "gene.b0874"
entity_type: "gene"
name: "lysO"
source_database: "NCBI RefSeq"
source_id: "gene-b0874"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0874"
  - "lysO"
---

# lysO

`gene.b0874`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0874`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lysO (gene.b0874) is a gene entity. It encodes lysO (protein.P75826). Encoded protein function: FUNCTION: Mediates export of lysine. {ECO:0000269|PubMed:25845847}. EcoCyc product frame: G6458-MONOMER. EcoCyc synonyms: ybjE. Genomic coordinates: 913958-914857. EcoCyc protein note: LysO is an L-lysine/thialysine efflux transporter. A ΔlysO strain has an increased intracellular concentration of L-lysine and impaired growth in the presence of the dipeptide Lys-Ala (but not in the presence of Arg-Ala); a ΔlysO strain is sensitive to the naturally occurring lysine antimetabolite, thialysine . LysO may export thialysine with higher affinity than L-lysine; LysO exports thialysine via proton-coupled antiport . Overexpression of lysO from a plasmid mediates increased export of L-lysine in Lys-Ala containing medium and mediates increased resistance to thialysine; overexpression of lysO from a plasmid suppresses the canavanine supersensitive phenotype of a strain lacking the arginine efflux transporter, ArgO possibly because increased extracellular lysine inhibits canavanine uptake by the ABC-3-CPLX . The cis-regulatory region of lysO contains an imperfect ArgR binding site; arginine mediates transcriptional repression of lysO via the ArgR repressor however this effect may only be evident when the cytoplasmic level of arginine is high...

## Biological Role

Repressed by argR (protein.P0A6D0). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75826|protein.P75826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lysO; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=lysO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002966,ECOCYC:G6458,GeneID:947142`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:913958-914857:-; feature_type=gene
