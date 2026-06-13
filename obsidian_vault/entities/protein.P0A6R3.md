---
entity_id: "protein.P0A6R3"
entity_type: "protein"
name: "fis"
source_database: "UniProt"
source_id: "P0A6R3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fis b3261 JW3229"
---

# fis

`protein.P0A6R3`

## Static

- Type: `protein`
- Source: `UniProt:P0A6R3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000269|PubMed:21903814}. Note=Scattered throughout the nucleoid (PubMed:21903814). {ECO:0000269|PubMed:21903814}.

## Enriched Summary

FUNCTION: Activates ribosomal RNA transcription, as well other genes. Plays a direct role in upstream activation of rRNA promoters. Binds to a recombinational enhancer sequence that is required to stimulate hin-mediated DNA inversion. Prevents initiation of DNA replication from oriC. Binds to hundreds of transcriptionally active and inactive AT-rich sites, approximately half its binding sites are in non-coding DNA, which only accounts for about 10% of the genome (PubMed:16963779). {ECO:0000269|PubMed:16963779, ECO:0000269|PubMed:2209559, ECO:0000269|PubMed:8836178}.

## Biological Role

Component of DNA-binding transcriptional dual regulator Fis (complex.ecocyc.CPLX0-7705).

## Annotation

FUNCTION: Activates ribosomal RNA transcription, as well other genes. Plays a direct role in upstream activation of rRNA promoters. Binds to a recombinational enhancer sequence that is required to stimulate hin-mediated DNA inversion. Prevents initiation of DNA replication from oriC. Binds to hundreds of transcriptionally active and inactive AT-rich sites, approximately half its binding sites are in non-coding DNA, which only accounts for about 10% of the genome (PubMed:16963779). {ECO:0000269|PubMed:16963779, ECO:0000269|PubMed:2209559, ECO:0000269|PubMed:8836178}.

## Outgoing Edges (153)

- `activates` --> [[gene.b0116|gene.b0116]] `RegulonDB` `S` - regulator=Fis; target=lpd; function=+
- `activates` --> [[gene.b0201|gene.b0201]] `RegulonDB` `S` - regulator=Fis; target=rrsH; function=+
- `activates` --> [[gene.b0202|gene.b0202]] `RegulonDB` `S` - regulator=Fis; target=ileV; function=+
- `activates` --> [[gene.b0203|gene.b0203]] `RegulonDB` `S` - regulator=Fis; target=alaV; function=+
- `activates` --> [[gene.b0204|gene.b0204]] `RegulonDB` `S` - regulator=Fis; target=rrlH; function=+
- `activates` --> [[gene.b0205|gene.b0205]] `RegulonDB` `S` - regulator=Fis; target=rrfH; function=+
- `activates` --> [[gene.b0405|gene.b0405]] `RegulonDB` `S` - regulator=Fis; target=queA; function=+
- `activates` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=Fis; target=ptsG; function=-+
- `activates` --> [[gene.b1109|gene.b1109]] `RegulonDB` `C` - regulator=Fis; target=ndh; function=-+
- `activates` --> [[gene.b1229|gene.b1229]] `RegulonDB` `C` - regulator=Fis; target=tpr; function=+
- `activates` --> [[gene.b1230|gene.b1230]] `RegulonDB` `C` - regulator=Fis; target=tyrV; function=+
- `activates` --> [[gene.b1231|gene.b1231]] `RegulonDB` `C` - regulator=Fis; target=tyrT; function=+
- `activates` --> [[gene.b1237|gene.b1237]] `RegulonDB` `S` - regulator=Fis; target=hns; function=+
- `activates` --> [[gene.b1241|gene.b1241]] `RegulonDB` `S` - regulator=Fis; target=adhE; function=+
- `activates` --> [[gene.b1274|gene.b1274]] `RegulonDB` `C` - regulator=Fis; target=topA; function=-+
- `activates` --> [[gene.b1530|gene.b1530]] `RegulonDB` `C` - regulator=Fis; target=marR; function=+
- `activates` --> [[gene.b1531|gene.b1531]] `RegulonDB` `C` - regulator=Fis; target=marA; function=+
- `activates` --> [[gene.b1532|gene.b1532]] `RegulonDB` `C` - regulator=Fis; target=marB; function=+
- `activates` --> [[gene.b2234|gene.b2234]] `RegulonDB` `S` - regulator=Fis; target=nrdA; function=+
- `activates` --> [[gene.b2235|gene.b2235]] `RegulonDB` `C` - regulator=Fis; target=nrdB; function=+
- `activates` --> [[gene.b2236|gene.b2236]] `RegulonDB` `S` - regulator=Fis; target=yfaE; function=+
- `activates` --> [[gene.b2239|gene.b2239]] `RegulonDB` `S` - regulator=Fis; target=glpQ; function=+
- `activates` --> [[gene.b2276|gene.b2276]] `RegulonDB` `S` - regulator=Fis; target=nuoN; function=+
- `activates` --> [[gene.b2277|gene.b2277]] `RegulonDB` `S` - regulator=Fis; target=nuoM; function=+
- `activates` --> [[gene.b2278|gene.b2278]] `RegulonDB` `S` - regulator=Fis; target=nuoL; function=+
- `activates` --> [[gene.b2279|gene.b2279]] `RegulonDB` `S` - regulator=Fis; target=nuoK; function=+
- `activates` --> [[gene.b2280|gene.b2280]] `RegulonDB` `S` - regulator=Fis; target=nuoJ; function=+
- `activates` --> [[gene.b2281|gene.b2281]] `RegulonDB` `S` - regulator=Fis; target=nuoI; function=+
- `activates` --> [[gene.b2282|gene.b2282]] `RegulonDB` `S` - regulator=Fis; target=nuoH; function=+
- `activates` --> [[gene.b2283|gene.b2283]] `RegulonDB` `S` - regulator=Fis; target=nuoG; function=+
- `activates` --> [[gene.b2284|gene.b2284]] `RegulonDB` `S` - regulator=Fis; target=nuoF; function=+
- `activates` --> [[gene.b2285|gene.b2285]] `RegulonDB` `S` - regulator=Fis; target=nuoE; function=+
- `activates` --> [[gene.b2286|gene.b2286]] `RegulonDB` `S` - regulator=Fis; target=nuoC; function=+
- `activates` --> [[gene.b2287|gene.b2287]] `RegulonDB` `S` - regulator=Fis; target=nuoB; function=+
- `activates` --> [[gene.b2288|gene.b2288]] `RegulonDB` `S` - regulator=Fis; target=nuoA; function=+
- `activates` --> [[gene.b2401|gene.b2401]] `RegulonDB` `C` - regulator=Fis; target=valU; function=+
- `activates` --> [[gene.b2402|gene.b2402]] `RegulonDB` `C` - regulator=Fis; target=valX; function=+
- `activates` --> [[gene.b2403|gene.b2403]] `RegulonDB` `C` - regulator=Fis; target=valY; function=+
- `activates` --> [[gene.b2404|gene.b2404]] `RegulonDB` `C` - regulator=Fis; target=lysV; function=+
- `activates` --> [[gene.b2579|gene.b2579]] `RegulonDB` `S` - regulator=Fis; target=grcA; function=+
- `activates` --> [[gene.b2588|gene.b2588]] `RegulonDB` `S` - regulator=Fis; target=rrfG; function=+
- `activates` --> [[gene.b2589|gene.b2589]] `RegulonDB` `S` - regulator=Fis; target=rrlG; function=+
- `activates` --> [[gene.b2590|gene.b2590]] `RegulonDB` `S` - regulator=Fis; target=gltW; function=+
- `activates` --> [[gene.b2591|gene.b2591]] `RegulonDB` `S` - regulator=Fis; target=rrsG; function=+
- `activates` --> [[gene.b2781|gene.b2781]] `RegulonDB` `C` - regulator=Fis; target=mazG; function=+
- `activates` --> [[gene.b2782|gene.b2782]] `RegulonDB` `C` - regulator=Fis; target=mazF; function=+
- `activates` --> [[gene.b2783|gene.b2783]] `RegulonDB` `C` - regulator=Fis; target=mazE; function=+
- `activates` --> [[gene.b2911|gene.b2911]] `RegulonDB` `S` - regulator=Fis; target=ssrS; function=-+
- `activates` --> [[gene.b2912|gene.b2912]] `RegulonDB` `S` - regulator=Fis; target=fau; function=-+
- `activates` --> [[gene.b3123|gene.b3123]] `RegulonDB` `S` - regulator=Fis; target=rnpB; function=-+
- `activates` --> [[gene.b3274|gene.b3274]] `RegulonDB` `S` - regulator=Fis; target=rrfD; function=+
- `activates` --> [[gene.b3276|gene.b3276]] `RegulonDB` `S` - regulator=Fis; target=alaU; function=+
- `activates` --> [[gene.b3278|gene.b3278]] `RegulonDB` `S` - regulator=Fis; target=rrsD; function=+
- `activates` --> [[gene.b3756|gene.b3756]] `RegulonDB` `S` - regulator=Fis; target=rrsC; function=+
- `activates` --> [[gene.b3757|gene.b3757]] `RegulonDB` `S` - regulator=Fis; target=gltU; function=+
- `activates` --> [[gene.b3758|gene.b3758]] `RegulonDB` `S` - regulator=Fis; target=rrlC; function=+
- `activates` --> [[gene.b3759|gene.b3759]] `RegulonDB` `S` - regulator=Fis; target=rrfC; function=+
- `activates` --> [[gene.b3845|gene.b3845]] `RegulonDB` `S` - regulator=Fis; target=fadA; function=+
- `activates` --> [[gene.b3846|gene.b3846]] `RegulonDB` `S` - regulator=Fis; target=fadB; function=+
- `activates` --> [[gene.b3851|gene.b3851]] `RegulonDB` `S` - regulator=Fis; target=rrsA; function=+
- `activates` --> [[gene.b3852|gene.b3852]] `RegulonDB` `S` - regulator=Fis; target=ileT; function=+
- `activates` --> [[gene.b3853|gene.b3853]] `RegulonDB` `S` - regulator=Fis; target=alaT; function=+
- `activates` --> [[gene.b3854|gene.b3854]] `RegulonDB` `S` - regulator=Fis; target=rrlA; function=+
- `activates` --> [[gene.b3855|gene.b3855]] `RegulonDB` `S` - regulator=Fis; target=rrfA; function=+
- `activates` --> [[gene.b3868|gene.b3868]] `RegulonDB` `C` - regulator=Fis; target=glnG; function=+
- `activates` --> [[gene.b3869|gene.b3869]] `RegulonDB` `C` - regulator=Fis; target=glnL; function=+
- `activates` --> [[gene.b3870|gene.b3870]] `RegulonDB` `C` - regulator=Fis; target=glnA; function=+
- `activates` --> [[gene.b3968|gene.b3968]] `RegulonDB` `S` - regulator=Fis; target=rrsB; function=+
- `activates` --> [[gene.b3969|gene.b3969]] `RegulonDB` `S` - regulator=Fis; target=gltT; function=+
- `activates` --> [[gene.b3970|gene.b3970]] `RegulonDB` `S` - regulator=Fis; target=rrlB; function=+
- `activates` --> [[gene.b3971|gene.b3971]] `RegulonDB` `S` - regulator=Fis; target=rrfB; function=+
- `activates` --> [[gene.b3976|gene.b3976]] `RegulonDB` `C` - regulator=Fis; target=thrU; function=+
- `activates` --> [[gene.b3977|gene.b3977]] `RegulonDB` `C` - regulator=Fis; target=tyrU; function=+
- `activates` --> [[gene.b3978|gene.b3978]] `RegulonDB` `C` - regulator=Fis; target=glyT; function=+
- `activates` --> [[gene.b3979|gene.b3979]] `RegulonDB` `C` - regulator=Fis; target=thrT; function=+
- `activates` --> [[gene.b3980|gene.b3980]] `RegulonDB` `C` - regulator=Fis; target=tufB; function=+
- `activates` --> [[gene.b4000|gene.b4000]] `RegulonDB` `S` - regulator=Fis; target=hupA; function=+
- `activates` --> [[gene.b4007|gene.b4007]] `RegulonDB` `S` - regulator=Fis; target=rrsE; function=+
- `activates` --> [[gene.b4008|gene.b4008]] `RegulonDB` `S` - regulator=Fis; target=gltV; function=+
- `activates` --> [[gene.b4009|gene.b4009]] `RegulonDB` `S` - regulator=Fis; target=rrlE; function=+
- `activates` --> [[gene.b4010|gene.b4010]] `RegulonDB` `S` - regulator=Fis; target=rrfE; function=+
- `activates` --> [[gene.b4032|gene.b4032]] `RegulonDB` `S` - regulator=Fis; target=malG; function=+
- `activates` --> [[gene.b4033|gene.b4033]] `RegulonDB` `S` - regulator=Fis; target=malF; function=+
- `activates` --> [[gene.b4034|gene.b4034]] `RegulonDB` `S` - regulator=Fis; target=malE; function=+
- `activates` --> [[gene.b4111|gene.b4111]] `RegulonDB` `C` - regulator=Fis; target=proP; function=+
- `activates` --> [[gene.b4314|gene.b4314]] `RegulonDB` `S` - regulator=Fis; target=fimA; function=+
- `activates` --> [[gene.b4315|gene.b4315]] `RegulonDB` `S` - regulator=Fis; target=fimI; function=+
- `activates` --> [[gene.b4316|gene.b4316]] `RegulonDB` `S` - regulator=Fis; target=fimC; function=+
- `activates` --> [[gene.b4317|gene.b4317]] `RegulonDB` `S` - regulator=Fis; target=fimD; function=+
- `activates` --> [[gene.b4318|gene.b4318]] `RegulonDB` `S` - regulator=Fis; target=fimF; function=+
- `activates` --> [[gene.b4319|gene.b4319]] `RegulonDB` `S` - regulator=Fis; target=fimG; function=+
- `activates` --> [[gene.b4320|gene.b4320]] `RegulonDB` `S` - regulator=Fis; target=fimH; function=+
- `activates` --> [[gene.b4368|gene.b4368]] `RegulonDB` `S` - regulator=Fis; target=leuV; function=+
- `activates` --> [[gene.b4369|gene.b4369]] `RegulonDB` `S` - regulator=Fis; target=leuP; function=+
- `activates` --> [[gene.b4370|gene.b4370]] `RegulonDB` `S` - regulator=Fis; target=leuQ; function=+
- `activates` --> [[gene.b4807|gene.b4807]] `RegulonDB` `S` - regulator=Fis; target=malH; function=+
- `activates` --> [[gene.b4836|gene.b4836]] `RegulonDB` `C` - regulator=Fis; target=glnZ; function=+
- `activates` --> [[gene.b4838|gene.b4838]] `RegulonDB` `S` - regulator=Fis; target=fimR2; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-7705|complex.ecocyc.CPLX0-7705]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0118|gene.b0118]] `RegulonDB` `S` - regulator=Fis; target=acnB; function=-
- `represses` --> [[gene.b0440|gene.b0440]] `RegulonDB` `S` - regulator=Fis; target=hupB; function=-
- `represses` --> [[gene.b0812|gene.b0812]] `RegulonDB` `S` - regulator=Fis; target=dps; function=-
- `represses` --> [[gene.b0999|gene.b0999]] `RegulonDB` `C` - regulator=Fis; target=cbpM; function=-
- `represses` --> [[gene.b1000|gene.b1000]] `RegulonDB` `C` - regulator=Fis; target=cbpA; function=-
- `represses` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=Fis; target=ptsG; function=-+
- `represses` --> [[gene.b1109|gene.b1109]] `RegulonDB` `C` - regulator=Fis; target=ndh; function=-+
- `represses` --> [[gene.b1182|gene.b1182]] `RegulonDB` `S` - regulator=Fis; target=hlyE; function=-
- `represses` --> [[gene.b1274|gene.b1274]] `RegulonDB` `C` - regulator=Fis; target=topA; function=-+
- `represses` --> [[gene.b1335|gene.b1335]] `RegulonDB` `S` - regulator=Fis; target=ogt; function=-
- `represses` --> [[gene.b1739|gene.b1739]] `RegulonDB` `S` - regulator=Fis; target=osmE; function=-
- `represses` --> [[gene.b1796|gene.b1796]] `RegulonDB` `S` - regulator=Fis; target=yoaG; function=-
- `represses` --> [[gene.b1797|gene.b1797]] `RegulonDB` `S` - regulator=Fis; target=yeaR; function=-
- `represses` --> [[gene.b2231|gene.b2231]] `RegulonDB` `S` - regulator=Fis; target=gyrA; function=-
- `represses` --> [[gene.b2400|gene.b2400]] `RegulonDB` `C` - regulator=Fis; target=gltX; function=-
- `represses` --> [[gene.b2507|gene.b2507]] `RegulonDB` `C` - regulator=Fis; target=guaA; function=-
- `represses` --> [[gene.b2508|gene.b2508]] `RegulonDB` `C` - regulator=Fis; target=guaB; function=-
- `represses` --> [[gene.b2911|gene.b2911]] `RegulonDB` `S` - regulator=Fis; target=ssrS; function=-+
- `represses` --> [[gene.b2912|gene.b2912]] `RegulonDB` `S` - regulator=Fis; target=fau; function=-+
- `represses` --> [[gene.b2980|gene.b2980]] `RegulonDB` `S` - regulator=Fis; target=glcC; function=-
- `represses` --> [[gene.b3123|gene.b3123]] `RegulonDB` `S` - regulator=Fis; target=rnpB; function=-+
- `represses` --> [[gene.b3221|gene.b3221]] `RegulonDB` `S` - regulator=Fis; target=nanQ; function=-
- `represses` --> [[gene.b3222|gene.b3222]] `RegulonDB` `S` - regulator=Fis; target=nanK; function=-
- `represses` --> [[gene.b3223|gene.b3223]] `RegulonDB` `S` - regulator=Fis; target=nanE; function=-
- `represses` --> [[gene.b3224|gene.b3224]] `RegulonDB` `S` - regulator=Fis; target=nanT; function=-
- `represses` --> [[gene.b3225|gene.b3225]] `RegulonDB` `S` - regulator=Fis; target=nanA; function=-
- `represses` --> [[gene.b3260|gene.b3260]] `RegulonDB` `C` - regulator=Fis; target=dusB; function=-
- `represses` --> [[gene.b3261|gene.b3261]] `RegulonDB` `C` - regulator=Fis; target=fis; function=-
- `represses` --> [[gene.b3357|gene.b3357]] `RegulonDB` `C` - regulator=Fis; target=crp; function=-
- `represses` --> [[gene.b3365|gene.b3365]] `RegulonDB` `C` - regulator=Fis; target=nirB; function=-
- `represses` --> [[gene.b3366|gene.b3366]] `RegulonDB` `S` - regulator=Fis; target=nirD; function=-
- `represses` --> [[gene.b3367|gene.b3367]] `RegulonDB` `S` - regulator=Fis; target=nirC; function=-
- `represses` --> [[gene.b3368|gene.b3368]] `RegulonDB` `S` - regulator=Fis; target=cysG; function=-
- `represses` --> [[gene.b3588|gene.b3588]] `RegulonDB` `C` - regulator=Fis; target=aldB; function=-
- `represses` --> [[gene.b3599|gene.b3599]] `RegulonDB` `S` - regulator=Fis; target=mtlA; function=-
- `represses` --> [[gene.b3600|gene.b3600]] `RegulonDB` `S` - regulator=Fis; target=mtlD; function=-
- `represses` --> [[gene.b3601|gene.b3601]] `RegulonDB` `S` - regulator=Fis; target=mtlR; function=-
- `represses` --> [[gene.b3699|gene.b3699]] `RegulonDB` `S` - regulator=Fis; target=gyrB; function=-
- `represses` --> [[gene.b3700|gene.b3700]] `RegulonDB` `C` - regulator=Fis; target=recF; function=-
- `represses` --> [[gene.b3701|gene.b3701]] `RegulonDB` `C` - regulator=Fis; target=dnaN; function=-
- `represses` --> [[gene.b3702|gene.b3702]] `RegulonDB` `C` - regulator=Fis; target=dnaA; function=-
- `represses` --> [[gene.b3721|gene.b3721]] `RegulonDB` `S` - regulator=Fis; target=bglB; function=-
- `represses` --> [[gene.b3722|gene.b3722]] `RegulonDB` `S` - regulator=Fis; target=bglF; function=-
- `represses` --> [[gene.b3723|gene.b3723]] `RegulonDB` `S` - regulator=Fis; target=bglG; function=-
- `represses` --> [[gene.b4067|gene.b4067]] `RegulonDB` `C` - regulator=Fis; target=actP; function=-
- `represses` --> [[gene.b4068|gene.b4068]] `RegulonDB` `S` - regulator=Fis; target=yjcH; function=-
- `represses` --> [[gene.b4069|gene.b4069]] `RegulonDB` `C` - regulator=Fis; target=acs; function=-
- `represses` --> [[gene.b4070|gene.b4070]] `RegulonDB` `S` - regulator=Fis; target=nrfA; function=-
- `represses` --> [[gene.b4071|gene.b4071]] `RegulonDB` `S` - regulator=Fis; target=nrfB; function=-
- `represses` --> [[gene.b4072|gene.b4072]] `RegulonDB` `S` - regulator=Fis; target=nrfC; function=-
- `represses` --> [[gene.b4073|gene.b4073]] `RegulonDB` `S` - regulator=Fis; target=nrfD; function=-
- `represses` --> [[gene.b4074|gene.b4074]] `RegulonDB` `S` - regulator=Fis; target=nrfE; function=-
- `represses` --> [[gene.b4075|gene.b4075]] `RegulonDB` `S` - regulator=Fis; target=nrfF; function=-
- `represses` --> [[gene.b4076|gene.b4076]] `RegulonDB` `S` - regulator=Fis; target=nrfG; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3261|gene.b3261]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A6R3`
- `KEGG:ecj:JW3229;eco:b3261;ecoc:C3026_17740;`
- `GeneID:947697;99707750;99864764;`
- `GO:GO:0000786; GO:0000976; GO:0001046; GO:0001216; GO:0001217; GO:0003677; GO:0005829; GO:0006351; GO:0006355; GO:0009295; GO:0009314; GO:0031421; GO:0032359; GO:0032993; GO:0042803; GO:0043565; GO:0044374; GO:0045911; GO:0051276`

## Notes

DNA-binding protein Fis (Factor-for-inversion stimulation protein) (Hin recombinational enhancer-binding protein)
