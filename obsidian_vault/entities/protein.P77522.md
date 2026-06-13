---
entity_id: "protein.P77522"
entity_type: "protein"
name: "sufB"
source_database: "UniProt"
source_id: "P77522"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sufB ynhE b1683 JW5273"
---

# sufB

`protein.P77522`

## Static

- Type: `protein`
- Source: `UniProt:P77522`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}. The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. The SufE protein transfers sulfur to SufB , which is a component of the SufBC2D Fe-S cluster assembly scaffold complex. The SufBCD complex activates the cysteine desulfurase activity of SufSE, likely by acting as the sulfur acceptor . The Cys405 residue of SufB and the His360 residue of SufD, located next to each other at the SufB-SufD interface, are required for Fe-S cluster assembly . The Cys254 residue of SufB is required for transfer of sulfur from SufE. C405 and E434 of SufB, both located at the SufB-SufD interface, appear to be part of the site of Fe-S cluster formation; a potential tunnel in the β-helix core domain may enable sulfur transfer from C254 to C405. In contrast, the CxxCxxxC motif comprised of C96, C99, and C103, is not required for in vivo function of SufB...

## Biological Role

Component of SufBC2D Fe-S cluster scaffold complex (complex.ecocyc.CPLX0-1341).

## Annotation

FUNCTION: The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1341|complex.ecocyc.CPLX0-1341]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1683|gene.b1683]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77522`
- `KEGG:ecj:JW5273;eco:b1683;ecoc:C3026_09640;`
- `GeneID:93775838;945753;`
- `GO:GO:0016226; GO:0051537; GO:0051539; GO:1990229`

## Notes

Iron-sulfur cluster assembly protein SufB
