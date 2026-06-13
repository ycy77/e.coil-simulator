---
entity_id: "protein.P0A700"
entity_type: "protein"
name: "hypA"
source_database: "UniProt"
source_id: "P0A700"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22016389}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hypA b2726 JW2696"
---

# hypA

`protein.P0A700`

## Static

- Type: `protein`
- Source: `UniProt:P0A700`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22016389}.

## Enriched Summary

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:12081959, PubMed:15995183). Mediates transfer of nickel, but not zinc, from the low-affinity metal-binding site in the GTPase domain of HypB to HypA (PubMed:23899293, PubMed:27951644). HypA is involved in maturation of hydrogenase 3. It may partially substitute for the function of HybF and vice versa (PubMed:12081959). May act as a scaffold for assembly of the nickel insertion proteins with the hydrogenase precursor protein after delivery of the iron center (PubMed:22016389). {ECO:0000269|PubMed:12081959, ECO:0000269|PubMed:15995183, ECO:0000269|PubMed:22016389, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644}. HypA and its homolog, HybF, are involved in the maturation of hydrogenase isozymes. A mutation in hypA almost completely abolishes hydrogenase 3 activity . HypA is specifically involved in hydrogenase 3 maturation, while HybF is involved in the maturation of hydrogenase 1 and 2; HypA and HybF can only partially substitute for each other . The presence of high levels of nickel can phenotypically rescue hypA and hybF mutants and a triple hypA hypB hybF mutant to a low level . HypA has both a nanomolar-affinity Zn2+ binding site and a micromolar-affinity Ni2+ binding site...

## Biological Role

Catalyzes RXN-22650 (reaction.ecocyc.RXN-22650). Component of HypA-HypB heterodimer (complex.ecocyc.CPLX0-3821).

## Annotation

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase (PubMed:12081959, PubMed:15995183). Mediates transfer of nickel, but not zinc, from the low-affinity metal-binding site in the GTPase domain of HypB to HypA (PubMed:23899293, PubMed:27951644). HypA is involved in maturation of hydrogenase 3. It may partially substitute for the function of HybF and vice versa (PubMed:12081959). May act as a scaffold for assembly of the nickel insertion proteins with the hydrogenase precursor protein after delivery of the iron center (PubMed:22016389). {ECO:0000269|PubMed:12081959, ECO:0000269|PubMed:15995183, ECO:0000269|PubMed:22016389, ECO:0000269|PubMed:23899293, ECO:0000269|PubMed:27951644}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-22650|reaction.ecocyc.RXN-22650]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-3821|complex.ecocyc.CPLX0-3821]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2726|gene.b2726]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A700`
- `KEGG:ecj:JW2696;eco:b2726;ecoc:C3026_15000;`
- `GeneID:93779282;947195;`
- `GO:GO:0005886; GO:0008270; GO:0016151; GO:0016530; GO:0042802; GO:0051604; GO:0065003; GO:1905360`

## Notes

Hydrogenase maturation factor HypA
