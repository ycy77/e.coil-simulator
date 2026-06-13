---
entity_id: "gene.b1981"
entity_type: "gene"
name: "shiA"
source_database: "NCBI RefSeq"
source_id: "gene-b1981"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1981"
  - "shiA"
---

# shiA

`gene.b1981`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1981`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

shiA (gene.b1981) is a gene entity. It encodes shiA (protein.P76350). Encoded protein function: FUNCTION: Involved in the uptake of shikimate, an intermediate in the aromatic amino acid biosynthetic pathway. {ECO:0000269|PubMed:9524262}. EcoCyc product frame: SHIA-MONOMER. EcoCyc synonyms: yeeM. Genomic coordinates: 2053643-2054959. EcoCyc protein note: ShiA has been implicated in the high affinity transport of shikimate, an intermediate in the aromatic amino acid biosynthetic pathway . Chromosomal mutants in shiA are unable to transport shikimate, and introduction of the cloned shiA gene restores shikimate transport . The ShiA protein has twelve predicted TMS and is a member of the major facilitator superfamily of transporters (MFS) and hence is likely to function as a proton/shikimate symporter. Analysis of a shiA-lacZ fusion has suggested that shiA expression is constitutive and is not regulated by the TyrR repressor . The shiA gene probably constitutes a monocistronic operon. Imported shikimate presumably serves as a substrate for biosynthesis of aromatic compounds.

## Biological Role

Repressed by nac (protein.Q47005). Activated by ryhB (gene.b4451), rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76350|protein.P76350]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[gene.b4451|gene.b4451]] `RegulonDB` `S` - regulator=RyhB; target=shiA; function=+
- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=shiA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=shiA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006572,ECOCYC:G7067,GeneID:946495`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2053643-2054959:+; feature_type=gene
