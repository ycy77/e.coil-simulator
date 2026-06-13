---
entity_id: "gene.b1828"
entity_type: "gene"
name: "yebQ"
source_database: "NCBI RefSeq"
source_id: "gene-b1828"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1828"
  - "yebQ"
---

# yebQ

`gene.b1828`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1828`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yebQ (gene.b1828) is a gene entity. It encodes yebQ (protein.P76269). Encoded protein function: Uncharacterized transporter YebQ EcoCyc product frame: B1828-MONOMER. Genomic coordinates: 1910276-1911649. EcoCyc protein note: Expression of cloned kdgR-yebQ in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) confers hypersensitivity to trimethoprim (minimum inhibitory concentration, 3.13 µg/mL for KAM3 versus 0.78 µg/mL for KAM3/pUCkdgR-yebQ) but overexpression of yebQ by itself (KAM3/pTrcHyebQ) does not result in a similar hypersensitivity phenotype and does not impact the resistance to a range of antibiotics, dyes and toxic compounds . yebQ is one of 35 efflux-encoding genes that have been deleted or inactivated in 'Efflux KnockOut-35' (EKO-35) - a K-12 BW25133-derived strain that lacks 35 efflux pumps and can be used as a platform to study their function . In the Transporter Classification Database, YebQ is a member of the Drug:H+ Antiporter-2 (DHA2) Family within the Major Facilitator Superfamily (MFS) .

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76269|protein.P76269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yebQ; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006085,ECOCYC:G7004,GeneID:946048`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1910276-1911649:+; feature_type=gene
