---
entity_id: "protein.P0A998"
entity_type: "protein"
name: "ftnA"
source_database: "UniProt"
source_id: "P0A998"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ftnA ftn gen-165 rsgA b1905 JW1893"
---

# ftnA

`protein.P0A998`

## Static

- Type: `protein`
- Source: `UniProt:P0A998`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Iron-storage protein. {ECO:0000269|PubMed:11254384}. ftnA encodes the iron-storage protein ferritin, which is similar to human ferritin H . Ferritin forms a multi-subunit, hollow spherical shell of 24 individual ferritin polypeptides that can sequester more than 2000 iron atoms in the center . Ferritin and CPLX0-1421 are distantly related . The crystal structure of ferritin has been determined, identifying three iron-binding sites per subunit . Two of these sites form a dinuclear iron center where oxidation of Fe(II) occurs, allowing iron to be stored as ferric phosphate . The third site appears to modulate Fe2+ binding to the dinuclear iron center . No protons are released upon initial binding of Fe2+. Subsequent oxidation of Fe2+ leads to production of H2O2, which is itself utilized for oxidation of Fe2+ bound at other ferroxidase centers . The iron core forms a hollow sphere in the presence of phosphate . In vitro, FtnA was shown to sequester iron released from damaged [2Fe-2S] clusters of IscU. Iron sequestered by FtnA can be transferred to IscA, but not IscU . Overexpression of ftnA rescues the oxygen sensitivity of a Δfur ΔrecA mutant, presumably by preventing toxic iron accumulation . An ftnA mutant shows impaired growth in iron-deficient media . Expression of ftnA is higher in stationary phase than log phase cells and is dependent on iron and Fur...

## Biological Role

Component of ferritin iron-storage complex (complex.ecocyc.CPLX0-3969).

## Annotation

FUNCTION: Iron-storage protein. {ECO:0000269|PubMed:11254384}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3969|complex.ecocyc.CPLX0-3969]] `EcoCyc` `database` - EcoCyc component coefficient=24 | EcoCyc protcplxs.col coefficient=24

## Incoming Edges (1)

- `encodes` <-- [[gene.b1905|gene.b1905]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A998`
- `KEGG:ecj:JW1893;eco:b1905;ecoc:C3026_10815;`
- `GeneID:86946760;93776210;946410;`
- `GO:GO:0004322; GO:0005737; GO:0005829; GO:0006826; GO:0006879; GO:0006974; GO:0006979; GO:0008198; GO:0008199; GO:0042802; GO:0071281; GO:0140315`
- `EC:1.16.3.2`

## Notes

Bacterial non-heme ferritin (EC 1.16.3.2) (Ferritin-1)
