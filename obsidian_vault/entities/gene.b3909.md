---
entity_id: "gene.b3909"
entity_type: "gene"
name: "kdgT"
source_database: "NCBI RefSeq"
source_id: "gene-b3909"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3909"
  - "kdgT"
---

# kdgT

`gene.b3909`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3909`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdgT (gene.b3909) is a gene entity. It encodes kdgT (protein.P0A712). Encoded protein function: FUNCTION: Catalyzes the proton-dependent uptake of 2-keto-3-deoxygluconate (KDG) into the cell (PubMed:15555, PubMed:6094479). Expression of this specific KDG-uptake system may allow growth with KDG as the sole carbon source (PubMed:4359651). Can also transport D-glucuronate (PubMed:15555, PubMed:6094479). {ECO:0000269|PubMed:15555, ECO:0000269|PubMed:6094479, ECO:0000303|PubMed:4359651}. EcoCyc product frame: KDGT-MONOMER. Genomic coordinates: 4101690-4102673. EcoCyc protein note: KdgT is a probable 2-keto-3-deoxy-D-gluconate (KDG) uptake system. The cloned kdgT gene increased uptake of KDG and to a lesser extent glucuronate and could complement the KDG transport defect in kdgT mutants. KDG transport has been shown in whole cells and membrane vesicles to be via proton symport . KdgT is the prototype representative of the KdgT family of KDG transporters. Expression of kdgT is inducible by KDG and is under the control of the KdgR repressor . Imported KDG is subsequently degraded to pyruvate and triose-phosphate.

## Biological Role

Repressed by glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A712|protein.P0A712]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=kdgT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012764,ECOCYC:EG11869,GeneID:948407`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4101690-4102673:+; feature_type=gene
