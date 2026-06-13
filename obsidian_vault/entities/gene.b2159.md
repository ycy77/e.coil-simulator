---
entity_id: "gene.b2159"
entity_type: "gene"
name: "nfo"
source_database: "NCBI RefSeq"
source_id: "gene-b2159"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2159"
  - "nfo"
---

# nfo

`gene.b2159`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2159`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nfo (gene.b2159) is a gene entity. It encodes nfo (protein.P0A6C1). Encoded protein function: FUNCTION: Endonuclease IV plays a role in DNA repair. It cleaves phosphodiester bonds at apurinic or apyrimidinic (AP) sites, generating a 3'-hydroxyl group and a 5'-terminal sugar phosphate. It preferentially attacks modified AP sites created by bleomycin and neocarzinostatin. EcoCyc product frame: EG10651-MONOMER. Genomic coordinates: 2250840-2251697. EcoCyc protein note: Endonuclease IV is an inducible apurinic/apyrimidinic (AP) site endonuclease. Early studies purified and characterized Endonuclease IV (Endo IV) from K-12 strains . Endo IV is induced when cells are grown in the presence of the DNA damaging agents, methyl viologen, and to a lesser extent, plumbagin, phenazine methosulfate and menadione . The purified enzyme catalyses AP endonuclease activity on plasmid DNA containing AP sites; it also exhibits 3'-phosphomonesterase and 3'-phosphodiesterase activity - releasing a variety of fragments from DNA 3'-termini, including phosphate, phosphoglycoaldehyde and deoxyribose 5-phosphate . The enzyme may or may not have 3'-5' exonuclease activity. Purified Endo IV is a metal-dependent endonuclease . Endo IV can incise the DNA backbone 5' of the oxidative lesion α-deoxyadenosine (see further )...

## Biological Role

Activated by soxS (protein.P0A9E2).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6C1|protein.P0A6C1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=nfo; function=+

## External IDs

- `Dbxref:ASAP:ABE-0007146,ECOCYC:EG10651,GeneID:946669`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2250840-2251697:+; feature_type=gene
