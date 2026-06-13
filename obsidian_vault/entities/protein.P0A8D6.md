---
entity_id: "protein.P0A8D6"
entity_type: "protein"
name: "ymdB"
source_database: "UniProt"
source_id: "P0A8D6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ymdB b1045 JW1032"
---

# ymdB

`protein.P0A8D6`

## Static

- Type: `protein`
- Source: `UniProt:P0A8D6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Deacetylates O-acetyl-ADP ribose to yield ADP-ribose and free acetate (PubMed:21257746, PubMed:26481419). Down-regulates ribonuclease 3 (RNase III) activity. Acts by interacting directly with the region of the ribonuclease that is required for dimerization/activation (PubMed:19141481). Overexpression inhibits biofilm formation via an RNase III-independent pathway. This inhibition is RpoS-dependent (PubMed:24267348, PubMed:28582517). Overexpression also results in increased susceptibility to apramycin (PubMed:28034758, PubMed:28582517). {ECO:0000269|PubMed:19141481, ECO:0000269|PubMed:21257746, ECO:0000269|PubMed:24267348, ECO:0000269|PubMed:26481419, ECO:0000269|PubMed:28034758, ECO:0000269|PubMed:28582517}. YmdB is a macrodomain family protein with O-acetyl-ADP-ribose deacetylase activity . O-acetyl-ADP-ribose is produced by NAD+-dependent protein deacetylation. The YmdB protein inhibits the activity of CPLX0-3281 by interacting directly with the enzyme. Amino acids 120-140 in the catalytic region of RNase III are necessary for YmdB binding . The interaction was modeled, and site-directed mutagenesis confirmed that residues R40 of YmdB and D128 of RNase III are important for the interaction . A protein inhibitor of RNase III was first identified by Makarov and Apirion . Crystal structures of YmdB have been solved, and a catalytic mechanism was proposed...

## Biological Role

Component of 2'-O-acetyl-ADP-ribose deacetylase, regulator of RNase III activity (complex.ecocyc.CPLX0-7758).

## Annotation

FUNCTION: Deacetylates O-acetyl-ADP ribose to yield ADP-ribose and free acetate (PubMed:21257746, PubMed:26481419). Down-regulates ribonuclease 3 (RNase III) activity. Acts by interacting directly with the region of the ribonuclease that is required for dimerization/activation (PubMed:19141481). Overexpression inhibits biofilm formation via an RNase III-independent pathway. This inhibition is RpoS-dependent (PubMed:24267348, PubMed:28582517). Overexpression also results in increased susceptibility to apramycin (PubMed:28034758, PubMed:28582517). {ECO:0000269|PubMed:19141481, ECO:0000269|PubMed:21257746, ECO:0000269|PubMed:24267348, ECO:0000269|PubMed:26481419, ECO:0000269|PubMed:28034758, ECO:0000269|PubMed:28582517}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7758|complex.ecocyc.CPLX0-7758]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1045|gene.b1045]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8D6`
- `KEGG:ecj:JW1032;eco:b1045;ecoc:C3026_06360;`
- `GeneID:93776369;946987;`
- `GO:GO:0001883; GO:0019899; GO:0042278; GO:0046677; GO:0060698; GO:0061463; GO:1900231`
- `EC:3.1.1.106`

## Notes

O-acetyl-ADP-ribose deacetylase (EC 3.1.1.106) (Regulator of RNase III activity)
