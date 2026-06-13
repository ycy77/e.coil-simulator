---
entity_id: "protein.P77689"
entity_type: "protein"
name: "sufD"
source_database: "UniProt"
source_id: "P77689"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sufD ynhC b1681 JW1671"
---

# sufD

`protein.P77689`

## Static

- Type: `protein`
- Source: `UniProt:P77689`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. Required for the stability of the FhuF protein. {ECO:0000269|PubMed:10322040, ECO:0000269|PubMed:12941942}. The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufD is a component of the SufBC2D Fe-S cluster assembly scaffold complex. Both SufC and SufD are required for Fe-S cluster formation on SufB in vivo. The SufD subunit is dispensible for sulfur transfer in vivo, but it is required for the acquisition of iron . The Cys405 residue of SufB and the His360 residue of SufD, located next to each other at the SufB-SufD interface, are required for Fe-S cluster assembly . A crystal structure of the SufC2-SufD2 complex has been determined at 2.2 Å resolution . A sufD, sufS or fhuF mutant exhibits a defect in utilization of a ferrioxamine B iron source . A sufD mutant exhibits unstable FhuF, compared to wild type, which precludes overproduction of FhuF...

## Biological Role

Component of SufBC2D Fe-S cluster scaffold complex (complex.ecocyc.CPLX0-1341).

## Annotation

FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. Required for the stability of the FhuF protein. {ECO:0000269|PubMed:10322040, ECO:0000269|PubMed:12941942}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1341|complex.ecocyc.CPLX0-1341]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1681|gene.b1681]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77689`
- `KEGG:ecj:JW1671;eco:b1681;ecoc:C3026_09630;`
- `GeneID:944878;`
- `GO:GO:0006979; GO:0016226; GO:1990229`

## Notes

Iron-sulfur cluster assembly protein SufD
