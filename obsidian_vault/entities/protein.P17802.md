---
entity_id: "protein.P17802"
entity_type: "protein"
name: "mutY"
source_database: "UniProt"
source_id: "P17802"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mutY micA b2961 JW2928"
---

# mutY

`protein.P17802`

## Static

- Type: `protein`
- Source: `UniProt:P17802`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Adenine glycosylase active on G-A mispairs. MutY also corrects error-prone DNA synthesis past GO lesions which are due to the oxidatively damaged form of guanine: 7,8-dihydro-8-oxoguanine (8-oxo-dGTP). {ECO:0000269|PubMed:1445834, ECO:0000269|PubMed:2682664}. MutY is a novel base excision repair (BER) glycosylase which catalyses the removal of adenine when it is paired with the oxidatively damaged form of guanine, CPD-12427 (GO; 8-oxoG); MutY activity prevents deleterious G:C → T:A transversion mutations. Strains defective in MutY function stimulate G:C → T:A transversion (see also ). Purified MutY is an A:G specific adenine glycosylase; MutY, a 5' endonuclease, and DNA polymerase I are able to reconstitute A:G → C:G mismatch correction in vitro . MutY removes adenines from 8-oxoG:A mispairs that result from trans-lesion DNA replication past 8-oxoG; MutY also removes adenine from A:C, and A:8-oxo-7,8-dihydrodeoxyadenine mispairs; MutY remains bound to the repair site which may prevent MutM from removing the 8-oxoG lesion with subsequent double strand break . MutY may or may not have associated apurinic/apyrimidinic endonuclease activity (see also ). Purified MutY removes guanine from 8-oxoG:G mispairs; strains defective in MutY function accumulate G:C → C:G transversions...

## Biological Role

Catalyzes RXN0-2661 (reaction.ecocyc.RXN0-2661). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

FUNCTION: Adenine glycosylase active on G-A mispairs. MutY also corrects error-prone DNA synthesis past GO lesions which are due to the oxidatively damaged form of guanine: 7,8-dihydro-8-oxoguanine (8-oxo-dGTP). {ECO:0000269|PubMed:1445834, ECO:0000269|PubMed:2682664}.

## Pathways

- `eco03410` Base excision repair (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-2661|reaction.ecocyc.RXN0-2661]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2961|gene.b2961]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17802`
- `KEGG:ecj:JW2928;eco:b2961;ecoc:C3026_16205;`
- `GeneID:947447;`
- `GO:GO:0000701; GO:0006284; GO:0006298; GO:0032357; GO:0034039; GO:0035485; GO:0046872; GO:0051539`
- `EC:3.2.2.31`

## Notes

Adenine DNA glycosylase (EC 3.2.2.31) (A/G-specific adenine glycosylase)
