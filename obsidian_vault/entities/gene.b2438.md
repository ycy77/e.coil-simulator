---
entity_id: "gene.b2438"
entity_type: "gene"
name: "eutK"
source_database: "NCBI RefSeq"
source_id: "gene-b2438"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2438"
  - "eutK"
---

# eutK

`gene.b2438`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2438`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

eutK (gene.b2438) is a gene entity. It encodes eutK (protein.P76540). Encoded protein function: FUNCTION: Probably a minor component of the bacterial microcompartment (BMC) shell dedicated to ethanolamine degradation. It might bind nucleic acids. {ECO:0000305|PubMed:20044574}. EcoCyc product frame: G7270-MONOMER. EcoCyc synonyms: yffI. Genomic coordinates: 2555228-2555728. EcoCyc protein note: The EutK protein consists of a BMC (bacterial microcompartment)-type domain followed by an additional C-terminal helix-turn-helix domain. Unlike the other BMC-type proteins (EutL, EutM and EutS), it behaves as a monomer in solution . The crystal structure of the C-terminal domain of EutK has been determined at 2.1 Å resolution. This domain forms a helix-turn-helix structure, suggesting that EutK binds nucleic acids . The function of the orthologous eut operon genes for ethanolamine utilization in Salmonella typhimurium have been studied experimentally . Expression of eutK does not change under anaerobiosis but decreases in an CPLX0-7797 FNR mutant strain (MC4100 Δfnr-2) compared to wild type; an FNR binding site is predicted upstream of eutK, but its location is not precisely identified .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76540|protein.P76540]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0008039,ECOCYC:G7270,GeneID:946912`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2555228-2555728:-; feature_type=gene
