---
entity_id: "gene.b2895"
entity_type: "gene"
name: "fldB"
source_database: "NCBI RefSeq"
source_id: "gene-b2895"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2895"
  - "fldB"
---

# fldB

`gene.b2895`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2895`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fldB (gene.b2895) is a gene entity. It encodes fldB (protein.P0ABY4). Encoded protein function: FUNCTION: Low-potential electron donor to a number of redox enzymes. {ECO:0000305}. EcoCyc product frame: OX-FLAVODOXIN2. Genomic coordinates: 3039855-3040376. EcoCyc protein note: Flavodoxin 2 (FldB) was discovered by sequence similarity to FLAVODOXIN1-MONOMER. Flavodoxins are small, acidic electron transfer proteins which contain FMN as a prosthetic group. The physiological role of FldB is so far unknown . Solution structures of apo- and holo-FldB have been obtained, showing a typical flavodoxin fold . fldB is a member of the SoxRS regulon. fldB expression is induced by paraquat, but an fldB mutant does not show increased sensitivity to paraquat. An fldB mutant has no obvious growth defect, and overexpression of fldB does not rescue the lethality of an fldA mutation .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABY4|protein.P0ABY4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fldB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009503,ECOCYC:EG12697,GeneID:947361`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3039855-3040376:+; feature_type=gene
