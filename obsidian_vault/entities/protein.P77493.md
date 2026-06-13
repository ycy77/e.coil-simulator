---
entity_id: "protein.P77493"
entity_type: "protein"
name: "ydjH"
source_database: "UniProt"
source_id: "P77493"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydjH b1772 JW5289"
---

# ydjH

`protein.P77493`

## Static

- Type: `protein`
- Source: `UniProt:P77493`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Sugar kinase that catalyzes the phosphorylation of 2-keto-monosaccharides at the C1 hydroxyl group (PubMed:31314509). It preferentially phosphorylates seven- to nine-carbon monosaccharides, relative to those with five or six carbons (PubMed:31314509). A terminal carboxylate is greatly preferred relative to those terminated with a phosphate (PubMed:31314509). The best substrate in vitro is L-glycero-L-galacto-octuluronate, yielding L-glycero-L-galacto-octuluronate-1-phosphate (PubMed:31314509). L-glycero-L-galacto-octuluronate is probably not the natural substrate, but it is highly likely that the physiological substrate has a very similar structure (PubMed:31314509). Is unable to efficiently catalyze the phosphorylation of ketoses that are phosphorylated at the terminal carbon (PubMed:31314509). {ECO:0000269|PubMed:31314509}.

## Biological Role

Component of L-glycero-L-galacto-octuluronate kinase (complex.ecocyc.CPLX0-8548).

## Annotation

FUNCTION: Sugar kinase that catalyzes the phosphorylation of 2-keto-monosaccharides at the C1 hydroxyl group (PubMed:31314509). It preferentially phosphorylates seven- to nine-carbon monosaccharides, relative to those with five or six carbons (PubMed:31314509). A terminal carboxylate is greatly preferred relative to those terminated with a phosphate (PubMed:31314509). The best substrate in vitro is L-glycero-L-galacto-octuluronate, yielding L-glycero-L-galacto-octuluronate-1-phosphate (PubMed:31314509). L-glycero-L-galacto-octuluronate is probably not the natural substrate, but it is highly likely that the physiological substrate has a very similar structure (PubMed:31314509). Is unable to efficiently catalyze the phosphorylation of ketoses that are phosphorylated at the terminal carbon (PubMed:31314509). {ECO:0000269|PubMed:31314509}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8548|complex.ecocyc.CPLX0-8548]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1772|gene.b1772]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77493`
- `KEGG:ecj:JW5289;eco:b1772;ecoc:C3026_10115;`
- `GeneID:75203078;946285;`
- `GO:GO:0005829; GO:0006974; GO:0008673; GO:0019200; GO:0019698; GO:0042803; GO:0042840`
- `EC:2.7.1.-`

## Notes

L-glycero-L-galacto-octuluronate kinase (EC 2.7.1.-)
