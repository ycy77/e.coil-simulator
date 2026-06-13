---
entity_id: "protein.P24193"
entity_type: "protein"
name: "hypE"
source_database: "UniProt"
source_id: "P24193"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hypE b2730 JW2700"
---

# hypE

`protein.P24193`

## Static

- Type: `protein`
- Source: `UniProt:P24193`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Along with HypF, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases. HypE catalyzes the ATP-dependent dehydration of the carboxamido group attached to its C-terminal cysteine to a cyano group (PubMed:12586941, PubMed:15291820). The cyano group is then transferred from HypE to the HypC-HypD complex or the HybG-HypD complex (PubMed:15504408). {ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:15504408}. HypE is one of the hydrogenase maturation proteins required for the assembly of the CN ligand of the NiFe metal center of FORMHYDROGI-CPLX, FORMHYDROG2-CPLX and HYDROG3-CPLX. At least seven gene products are involved in the maturation of hydrogenases, which includes the generation and incorporation of the CN ligand from carbamoylphosphate (CP). First, EG11551-MONOMER HypF converts CP and ATP to carbamoyladenylate, inorganic phosphate, pyrophosphate, and AMP . It then transfers the carbamoyl group to the carboxy terminal cysteine of HypE . During the carbamoyl transfer reaction, HypE and HypF form a tight stoichiometric complex where HypE catalyzes the ATP hydrolysis-dependent dehydration of the carbamate group to a cyanate group...

## Biological Role

Catalyzes RXN-17943 (reaction.ecocyc.RXN-17943), RXN-22648 (reaction.ecocyc.RXN-22648).

## Annotation

FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Along with HypF, it catalyzes the synthesis of the CN ligands of the active site iron of [NiFe]-hydrogenases. HypE catalyzes the ATP-dependent dehydration of the carboxamido group attached to its C-terminal cysteine to a cyano group (PubMed:12586941, PubMed:15291820). The cyano group is then transferred from HypE to the HypC-HypD complex or the HybG-HypD complex (PubMed:15504408). {ECO:0000269|PubMed:12586941, ECO:0000269|PubMed:15291820, ECO:0000269|PubMed:15504408}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17943|reaction.ecocyc.RXN-17943]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-22648|reaction.ecocyc.RXN-22648]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2730|gene.b2730]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P24193`
- `KEGG:ecj:JW2700;eco:b2730;ecoc:C3026_15020;`
- `GeneID:947182;`
- `GO:GO:0016829; GO:0051604; GO:0065003; GO:1904949`
- `EC:4.2.1.-`

## Notes

Carbamoyl dehydratase HypE (EC 4.2.1.-) (Hydrogenase maturation factor HypE)
