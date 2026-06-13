---
entity_id: "protein.P77499"
entity_type: "protein"
name: "sufC"
source_database: "UniProt"
source_id: "P77499"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12554644}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sufC ynhD b1682 JW1672"
---

# sufC

`protein.P77499`

## Static

- Type: `protein`
- Source: `UniProt:P77499`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12554644}.

## Enriched Summary

FUNCTION: Has low ATPase activity. The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12554644, ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}. The assembly of iron-sulfur clusters requires complex biosynthetic machinery. E. coli encodes two sets of proteins, the Isc and the Suf system, to achieve this task. SufC is a component of the SufBC2D Fe-S cluster assembly scaffold complex. SufC is a member of the ABC ATPase superfamily; its ATPase activity is required for iron acquisition in vivo, and both SufC and SufD are required for Fe-S cluster formation on SufB in vivo . A crystal structure of SufC has been determined at 2.5 Å resolution , and a crystal structure of the SufC2-SufD2 complex has been determined at 2.2 Å resolution . Upon associating with SufD, the structure of SufC changes to become competent for ATP binding and hydrolysis . Crystal structures of the SufBC2D complex have been solved. The SufB and SufD subunits form the center of the complex, and each is associated with one SufC subunit...

## Biological Role

Component of SufBC2D Fe-S cluster scaffold complex (complex.ecocyc.CPLX0-1341).

## Annotation

FUNCTION: Has low ATPase activity. The SufBCD complex acts synergistically with SufE to stimulate the cysteine desulfurase activity of SufS. The SufBCD complex contributes to the assembly or repair of oxygen-labile iron-sulfur clusters under oxidative stress. May facilitate iron uptake from extracellular iron chelators under iron limitation. {ECO:0000269|PubMed:12554644, ECO:0000269|PubMed:12941942, ECO:0000269|PubMed:19810706}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-1341|complex.ecocyc.CPLX0-1341]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1682|gene.b1682]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77499`
- `KEGG:ecj:JW1672;eco:b1682;ecoc:C3026_09635;`
- `GeneID:946128;`
- `GO:GO:0005524; GO:0005829; GO:0009314; GO:0016226; GO:0016887; GO:1990229`

## Notes

Probable ATP-dependent transporter SufC
