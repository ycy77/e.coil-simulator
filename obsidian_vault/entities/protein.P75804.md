---
entity_id: "protein.P75804"
entity_type: "protein"
name: "yliI"
source_database: "UniProt"
source_id: "P75804"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yliI b0837 JW0821"
---

# yliI

`protein.P75804`

## Static

- Type: `protein`
- Source: `UniProt:P75804`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:16522795}.

## Enriched Summary

FUNCTION: Aldose sugar dehydrogenase with broad substrate specificity. The physiological substrate is unknown. Can oxidize glucose to gluconolactone. Can also utilize D-arabinose, L-arabinose and 2-deoxy-glucose. Has higher activity towards oligomeric sugars, such as maltose, maltotriose or cellobiose. It may function to input sugar-derived electrons into the respiratory network. {ECO:0000269|PubMed:16864586}. YliI is an aldose sugar dehydrogenase that requires the cofactor pyrroloquinoline quinone (PQQ) for activity . E. coli lacks the ability to synthesize PQQ however, it exhibits chemotaxis towards environmental PQQ , and may thus use an externally supplied cofactor . PQQ is transported across the outer membrane by the TonB-dependent transporter G6762-MONOMER PqqU . The physiological substrate of YliI is unknown . YliI localizes to the the periplasm and is associated with the outer membrane under certain physiological conditions . Sequence similarity suggests that YliI may contain β-barrel structures ; however, the β-propeller fold of YliI may have led to a false-positive prediction of a β-barrel structure (von Heijne, pers. comm., 8/8/2006). The crystal structure of YliI has been determined at 1.5 Å resolution .

## Biological Role

Catalyzes RXN0-6371 (reaction.ecocyc.RXN0-6371). Bound by Ca2+ (molecule.ecocyc.CA_2), pyrroloquinoline quinone (molecule.ecocyc.PQQ).

## Annotation

FUNCTION: Aldose sugar dehydrogenase with broad substrate specificity. The physiological substrate is unknown. Can oxidize glucose to gluconolactone. Can also utilize D-arabinose, L-arabinose and 2-deoxy-glucose. Has higher activity towards oligomeric sugars, such as maltose, maltotriose or cellobiose. It may function to input sugar-derived electrons into the respiratory network. {ECO:0000269|PubMed:16864586}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6371|reaction.ecocyc.RXN0-6371]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.ecocyc.CA_2|molecule.ecocyc.CA_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.PQQ|molecule.ecocyc.PQQ]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0837|gene.b0837]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75804`
- `KEGG:ecj:JW0821;eco:b0837;ecoc:C3026_05240;`
- `GeneID:93776585;945467;`
- `GO:GO:0005509; GO:0009279; GO:0016901; GO:0030288; GO:0070968`
- `EC:1.1.5.-`

## Notes

Aldose sugar dehydrogenase YliI (Asd) (EC 1.1.5.-) (Soluble aldose sugar dehydrogenase YliI)
