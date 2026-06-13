---
entity_id: "gene.b0606"
entity_type: "gene"
name: "ahpF"
source_database: "NCBI RefSeq"
source_id: "gene-b0606"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0606"
  - "ahpF"
---

# ahpF

`gene.b0606`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0606`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ahpF (gene.b0606) is a gene entity. It encodes ahpF (protein.P35340). Encoded protein function: FUNCTION: Serves to protect the cell against DNA damage by alkyl hydroperoxides. It can use either NADH or NADPH as electron donor for direct reduction of redox dyes or of alkyl hydroperoxides when combined with the AhpC protein. EcoCyc product frame: EG11385-MONOMER. Genomic coordinates: 639753-641318. EcoCyc protein note: AhpF is the peroxiredoxin reductase component of alkyl hydroperoxide reductase, and is one of the ten most abundant proteins in TAX-562 . The N-terminal domain of AhpF belongs to the family of protein-disulfide oxidoreductases, while the C terminus belongs to the thioredoxin reductase family . By similarity to the enzyme from Salmonella typhimurium, it is thought to channel electrons from NADH to the AhpC component for reduction of the hydroperoxide substrate. An internal redox-active disulfide bridge between two cysteine residues is reduced by electron transfer from NADH via the FAD cofactor. This reduction triggers a cascade of disulfide-exchange reactions, first intramolecularly, then intermolecularly to the disulfide cysteine residues of the AhpC component. AhpF consists of an N-terminal domain (NTD), an FAD-binding domain and an NADH-binding domain . A crystal structure of the catalytic core of AhpF containing the FAD cofactor has been solved at 1...

## Biological Role

Activated by rpoD (protein.P00579), oxyR (protein.P0ACQ4), rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P35340|protein.P35340]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ahpF; function=+
- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `S` - regulator=OxyR; target=ahpF; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=ahpF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002093,ECOCYC:EG11385,GeneID:947540`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:639753-641318:+; feature_type=gene
