---
entity_id: "gene.b4173"
entity_type: "gene"
name: "hflX"
source_database: "NCBI RefSeq"
source_id: "gene-b4173"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4173"
  - "hflX"
---

# hflX

`gene.b4173`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4173`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hflX (gene.b4173) is a gene entity. It encodes hflX (protein.P25519). Encoded protein function: FUNCTION: GTPase that associates with the 50S ribosomal subunit and may have a role during protein synthesis or ribosome biogenesis. In vitro, also exhibits ATPase activity. {ECO:0000255|HAMAP-Rule:MF_00900, ECO:0000269|PubMed:19109926, ECO:0000269|PubMed:19181811, ECO:0000269|PubMed:19824612}. EcoCyc product frame: EG10437-MONOMER. EcoCyc synonyms: hslX, hflA. Genomic coordinates: 4400672-4401952. EcoCyc protein note: HflX is a heat shock-induced ribosome-dependent GTPase that rescues stalled ribosomes by dissociating vacant and mRNA-associated ribosomes with deacylated tRNA in the peptidyl site . Structural data suggests that HflX disrupts the central bridges between the ribosomal subunits and thereby promotes their dissociation . The HflX protein is a GTPase that interacts with the 50S subunit of the ribosome in the presence of both GTP, GDP, ATP and ADP . The intrinsic GTPase activity of HflX is very slow and can be stimulated 1000-fold by interaction with the 50S subunit as well as 70S ribosomes and poly(U)-programmed 70S ribosomes . GTP hydrolysis is required for ribosome dissociation or the release of HflX from the 50S subunit . HflX binds both GTP and ATP . Both the N-terminal and the C-terminal domain can bind and hydrolyze GTP and ATP...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579), rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25519|protein.P25519]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hflX; function=+
- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hflX; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=hflX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013661,ECOCYC:EG10437,GeneID:948688`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4400672-4401952:+; feature_type=gene
