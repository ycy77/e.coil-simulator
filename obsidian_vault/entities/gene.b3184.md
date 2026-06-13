---
entity_id: "gene.b3184"
entity_type: "gene"
name: "yhbE"
source_database: "NCBI RefSeq"
source_id: "gene-b3184"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3184"
  - "yhbE"
---

# yhbE

`gene.b3184`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3184`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhbE (gene.b3184) is a gene entity. It encodes yhbE (protein.P0AA73). Encoded protein function: Uncharacterized inner membrane transporter YhbE EcoCyc product frame: EG11499-MONOMER. Genomic coordinates: 3331770-3332735. EcoCyc protein note: YhbE is predicted to be an inner membrane protein with 10 transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . yhbE is expressed from an operon along with rplU, rpmA, and obgE under control of the rplU promoter. This operon is mainly expressed during exponential growth and is probably indirectly regulated by ppGpp/DksA . Furthermore, the amount of YhbE is affected by the presence of a terminator between rpmA and yhbE . Deletion of yhbE does not affect persister cell formation . In the Transporter Classification Database YhbE is a member of the Drug/Metabolite Exporter (DME) family within the Drug/Metabolite Transporter (DMT) superfamily.

## Biological Role

Activated by rpoD (protein.P00579), mlrA (protein.P33358).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AA73|protein.P0AA73]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhbE; function=+
- `activates` <-- [[protein.P33358|protein.P33358]] `RegulonDB` `S` - regulator=MlrA; target=yhbE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010464,ECOCYC:EG11499,GeneID:947699`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3331770-3332735:-; feature_type=gene
