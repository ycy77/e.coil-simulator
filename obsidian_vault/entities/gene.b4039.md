---
entity_id: "gene.b4039"
entity_type: "gene"
name: "ubiC"
source_database: "NCBI RefSeq"
source_id: "gene-b4039"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4039"
  - "ubiC"
---

# ubiC

`gene.b4039`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4039`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiC (gene.b4039) is a gene entity. It encodes ubiC (protein.P26602). Encoded protein function: FUNCTION: Removes the pyruvyl group from chorismate, with concomitant aromatization of the ring, to provide 4-hydroxybenzoate (4HB) for the ubiquinone pathway. {ECO:0000269|PubMed:11825618, ECO:0000269|PubMed:16343413, ECO:0000269|PubMed:1644758, ECO:0000269|PubMed:8012607}. EcoCyc product frame: CHORPYRLY-MONOMER. Genomic coordinates: 4252506-4253003. EcoCyc protein note: Chorismate pyruvate—lyase (CPL) catalyzes the first committed step in the biosynthesis of ubiquinone, the conversion of chorismate to 4-hydroxybenzoate . The enzyme retains and is efficiently inhibited by the 4-hydroxybenzoate reaction product, which may present a control mechanism for the ubiquinone biosynthesis pathway or a mechanism for delivery of 4-hydroxybenzoate to the membrane . Crystal structures of the enzyme in various forms have been solved; the structures have revealed the basis for tight product binding and the structural basis for the catalytic and product release mechanisms . A ubiC mutant can grow on glucose as the sole source of carbon, but can not grow on malate or succinate unless 4-hydroxybenzoate is provided . The growth yield of a ubiCA mutant grown aerobically on glucose or glycerol is much lower than that of wild-type...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P26602|protein.P26602]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0013227,ECOCYC:EG11369,GeneID:948545`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4252506-4253003:+; feature_type=gene
