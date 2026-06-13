---
entity_id: "gene.b4099"
entity_type: "gene"
name: "phnI"
source_database: "NCBI RefSeq"
source_id: "gene-b4099"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4099"
  - "phnI"
---

# phnI

`gene.b4099`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4099`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

phnI (gene.b4099) is a gene entity. It encodes phnI (protein.P16687). Encoded protein function: FUNCTION: Together with PhnG, PhnH and PhnL is required for the transfer of the ribose triphosphate moiety from ATP to methyl phosphonate. PhnI alone has nucleosidase activity, catalyzing the hydrolysis of ATP or GTP forming alpha-D-ribose 5-triphosphate and adenine or guanine, respectively. {ECO:0000269|PubMed:22089136}. EcoCyc product frame: EG10718-MONOMER. Genomic coordinates: 4319599-4320663. EcoCyc protein note: The phnI gene is part of a 14-gene phnCDEFGHIJKLMNOP operon that is involved in phosphonate uptake and metabolism and is a member of the phosphate regulon . A phnI mutant accumulates presumed intermediates of the C-P lyase pathway of phosphonate degradation . The PhnI protein alone has nucleosidase activity, producing D-ribose-5-triphosphate and the free base from GTP and ATP. However, in a mixture together with PhnG, PhnH and PhnL it catalyzes the nucleophilic attack of CPD0-1068 on the anomeric carbon of ATP to form adenine and CPD0-2479 . Immucillin-A triphosphate mimics the transition state structure for the nucleosidase reaction and inhibits PhnI activity . PhnI is a component of the CPLX0-10309 .

## Biological Role

Activated by rpoD (protein.P00579), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00440` Phosphonate and phosphinate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P16687|protein.P16687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=phnI; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=phnI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013428,ECOCYC:EG10718,GeneID:948605`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4319599-4320663:-; feature_type=gene
