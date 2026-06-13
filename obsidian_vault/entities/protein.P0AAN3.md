---
entity_id: "protein.P0AAN3"
entity_type: "protein"
name: "hypB"
source_database: "UniProt"
source_id: "P0AAN3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hypB b2727 JW2697"
---

# hypB

`protein.P0AAN3`

## Static

- Type: `protein`
- Source: `UniProt:P0AAN3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:7601092, PubMed:8756471). Exhibits a low intrinsic GTPase activity, which is essential for nickel insertion (PubMed:21544686, PubMed:27951644, PubMed:7601092). In the presence of GDP, nickel, but not zinc, is transferred from the HypB GTPase domain (G-domain) to HypA (PubMed:23899293, PubMed:27951644). {ECO:0000269|PubMed:21544686, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644, ECO:0000269|PubMed:7601092, ECO:0000269|PubMed:8756471}. The HypB protein is an accessory protein involved in the maturation of all hydrogenase isoenzymes. It is required for the incorporation of nickel into the large subunit of hydrogenases in vivo and in vitro . HypB binds Ni2+ with sub-picomolar KD in approximately stoichiometric amounts; the binding site was localized to the N-terminal CXXCGC motif and characterized extensively . A short peptide containing this motif retains Ni2+ binding activity . A low-affinity metal binding site with preference for Zn2+ exists in the C-terminal GTPase domain . Both sites are required for HypB activity . The N-terminal high affinity site can bind both Ni2+ and Zn2+; however, the coordination environment of the two metal ions differs...

## Biological Role

Catalyzes RXN-22957 (reaction.ecocyc.RXN-22957), RXN0-5462 (reaction.ecocyc.RXN0-5462). Component of hydrogenase isozymes Ni(2+) incorporation protein HypB (complex.ecocyc.CPLX0-3561), HypA-HypB heterodimer (complex.ecocyc.CPLX0-3821).

## Annotation

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:7601092, PubMed:8756471). Exhibits a low intrinsic GTPase activity, which is essential for nickel insertion (PubMed:21544686, PubMed:27951644, PubMed:7601092). In the presence of GDP, nickel, but not zinc, is transferred from the HypB GTPase domain (G-domain) to HypA (PubMed:23899293, PubMed:27951644). {ECO:0000269|PubMed:21544686, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644, ECO:0000269|PubMed:7601092, ECO:0000269|PubMed:8756471}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.RXN-22957|reaction.ecocyc.RXN-22957]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-3561|complex.ecocyc.CPLX0-3561]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3821|complex.ecocyc.CPLX0-3821]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2727|gene.b2727]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAN3`
- `KEGG:ecj:JW2697;eco:b2727;ecoc:C3026_15005;`
- `GeneID:93779281;947194;`
- `GO:GO:0003924; GO:0005525; GO:0008270; GO:0016151; GO:0016530; GO:0042803; GO:0051604; GO:0065003; GO:0097216; GO:1905360`

## Notes

Hydrogenase maturation factor HypB (Hydrogenase isoenzymes nickel incorporation protein HypB)
