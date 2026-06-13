---
entity_id: "gene.b4475"
entity_type: "gene"
name: "rtcA"
source_database: "NCBI RefSeq"
source_id: "gene-b4475"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4475"
  - "rtcA"
---

# rtcA

`gene.b4475`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4475`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rtcA (gene.b4475) is a gene entity. It encodes rtcA (protein.P46849). Encoded protein function: FUNCTION: Catalyzes the conversion of 3'-phosphate to a 2',3'-cyclic phosphodiester at the end of RNA. The mechanism of action of the enzyme occurs in 3 steps: (A) adenylation of the enzyme by ATP; (B) transfer of adenylate to an RNA-N3'P to produce RNA-N3'PP5'A; (C) and attack of the adjacent 2'-hydroxyl on the 3'-phosphorus in the diester linkage to produce the cyclic end product. Likely functions in some aspects of cellular RNA processing. {ECO:0000269|PubMed:9738023}. EcoCyc product frame: G7750-MONOMER. EcoCyc synonyms: yhgJ, yhgK, b3420, b3419. Genomic coordinates: 3555833-3556849. EcoCyc protein note: RNA 3'-terminal phosphate cyclase (RtcA) converts the 3'-terminal phosphate of various RNA substrates into the 2',3'-cyclic phosphodiester in an ATP-dependent reaction . The physiological role of the enzyme is unknown. Recently, it was shown that the enzyme also has a novel polynucleotide 5' adenylylation activity , which raises additional possibilities for its physiological function. RtcA can also act on RNA substrates with 2'-terminal phosphate ends, albeit at a dramatically lower rate. RtcA is proposed to be part of an RNA repair pathway, converting RNA 2'-phosphates, which are not substrates of RtcB, to 2',3'-cyclic phosphates that can be sealed...

## Biological Role

Activated by rpoN (protein.P24255).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P46849|protein.P46849]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `S` - sigma=sigma54; target=rtcA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0174104,ECOCYC:G7750,GeneID:2847707`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3555833-3556849:-; feature_type=gene
