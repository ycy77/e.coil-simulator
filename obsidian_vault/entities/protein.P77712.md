---
entity_id: "protein.P77712"
entity_type: "protein"
name: "fadM"
source_database: "UniProt"
source_id: "P77712"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fadM tesC ybaW b0443 JW0433"
---

# fadM

`protein.P77712`

## Static

- Type: `protein`
- Source: `UniProt:P77712`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Long-chain acyl-CoA thioesterase that could be involved in beta-oxidation of fatty acids (PubMed:18576672). Is most active with 3,5-tetradecadienoyl-CoA, a metabolite of oleic acid that is hydrolyzed during oleate beta-oxidation, but can also use other substrates such as 3,5-dodecadienoyl-CoA, 9-cis-octadecenoyl-CoA, octadecanoyl-CoA, hexadecanoyl-CoA, 3-hydroxytetradecanoyl-CoA and tetradecanoyl-CoA (PubMed:18576672). {ECO:0000269|PubMed:18576672}. Thioesterase III (FadM) is a long-chain acyl-CoA thioesterase that is involved in the β-oxidation of oleic acid. The enzyme is able to hydrolyze a number of related substrates. The best substrate is 3,5-tetradecadienoyl-CoA, which is a minor side product of oleate β-oxidation that is resistant to further degradation. The hydrolysis product, 3,5-tetradecadienoate, is released into the growth medium . Thioesterase III is expressed upon growth on oleic acid as the sole source of carbon . fadM is a member of the fad regulon; expression is induced by a number of fatty acids, with C18:1 as the best inducer . Reports disagree on whether or not conjugated linoleic acid (CLA) induces an even higher level of expression of fadM.

## Biological Role

Catalyzes RXN0-5390 (reaction.ecocyc.RXN0-5390).

## Annotation

FUNCTION: Long-chain acyl-CoA thioesterase that could be involved in beta-oxidation of fatty acids (PubMed:18576672). Is most active with 3,5-tetradecadienoyl-CoA, a metabolite of oleic acid that is hydrolyzed during oleate beta-oxidation, but can also use other substrates such as 3,5-dodecadienoyl-CoA, 9-cis-octadecenoyl-CoA, octadecanoyl-CoA, hexadecanoyl-CoA, 3-hydroxytetradecanoyl-CoA and tetradecanoyl-CoA (PubMed:18576672). {ECO:0000269|PubMed:18576672}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5390|reaction.ecocyc.RXN0-5390]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0443|gene.b0443]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77712`
- `KEGG:ecj:JW0433;eco:b0443;ecoc:C3026_02170;`
- `GeneID:93777007;945812;`
- `GO:GO:0006635; GO:0047617`
- `EC:3.1.2.-`

## Notes

Long-chain acyl-CoA thioesterase FadM (EC 3.1.2.-) (Acyl-CoA thioester hydrolase) (Thioesterase 3) (Thioesterase III)
