---
entity_id: "gene.b0336"
entity_type: "gene"
name: "codB"
source_database: "NCBI RefSeq"
source_id: "gene-b0336"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0336"
  - "codB"
---

# codB

`gene.b0336`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0336`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

codB (gene.b0336) is a gene entity. It encodes codB (protein.P0AA82). Encoded protein function: FUNCTION: Required for cytosine transport into the cell. EcoCyc product frame: CODB-MONOMER. Genomic coordinates: 354922-356181. EcoCyc protein note: CodB is a cytosine transporter which probably functions as a cytosine/proton symporter. Whole cell transport assays have shown that the cloned codB gene can complement mutants with cytosine transport defects which had mapped to a locus near the codA gene . The codB gene is located in a cytosine-inducible operon with the codA gene encoding cytosine deaminase . Consistent with this, CodB belongs to the NCS1 family of purine and pyrimidine transporters . Analysis of alkaline phosphatase and β-galactosidase fusions has suggested that CodB consists of twelve TMS . Imported cytosine can be metabolised via hydrolytic deamination by CodA to yield uracil and ammonia.

## Biological Role

Activated by rpoD (protein.P00579), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA82|protein.P0AA82]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=codB; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `C` - regulator=Nac; target=codB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001159,ECOCYC:EG11327,GeneID:944994`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:354922-356181:+; feature_type=gene
